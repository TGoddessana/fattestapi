from dataclasses import dataclass
from typing import Generic, Optional

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from fullask_rest_framework.repositories.sqlalchemy import \
    SQLAlchemyFullRepository
from fullask_rest_framework.vo.filtering import FilteringRequest
from fullask_rest_framework.vo.pagination import (PaginationRequest,
                                                  PaginationResponse)
from fullask_rest_framework.vo.sorting import SortingRequest

###################
# pytest fixtures #
###################

db = SQLAlchemy()


class UserModel(db.Model):  # type: ignore[name-defined]
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


@pytest.fixture
def user_repository():
    class UserRepository(SQLAlchemyFullRepository):
        @staticmethod
        def get_model():
            return UserModel

    yield UserRepository(db=db)


@pytest.fixture
def test_app():
    test_app = Flask("test_app")
    test_app.config["TESTING"] = True
    test_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db.init_app(test_app)

    with test_app.app_context():
        UserModel
        db.create_all()

    yield test_app


# ##################
# test code starts #
# ##################


def test_save_success_and_return_entity(test_app, user_repository):
    """
    Test that the save() method does a good job of saving.
    """
    user_fullask = UserModel(name="mr_fullask")
    with test_app.test_request_context():
        user_entity = user_repository.save(user_fullask)
        assert UserModel.query.count() == 1
        assert user_entity.id == 1
        assert user_entity.name == "mr_fullask"


def test_get_id_and_save_success(test_app, user_repository):
    """
    Get the entity with the read_by_id method, make your modifications, and then use the
    Test that the save() method does a good job of saving.
    """

    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        user_fullask = user_repository.read_by_id(1)
        user_fullask.name = "mr_django"
        user_repository.save(user_fullask)


def test_save_all_success_and_return_entities(test_app, user_repository):
    """
    Test that the save_all() method does a good job of saving.
    """
    user_fullask = UserModel(name="mr_fullask")
    user_django = UserModel(name="mr_django")
    user_fastapi = UserModel(name="mr_fastapi")
    with test_app.test_request_context():
        user_entities = user_repository.save_all(
            [user_fullask, user_django, user_fastapi]
        )
        assert UserModel.query.count() == 3
        assert isinstance(user_entities, list)
        assert user_entities[0].id == 1
        assert user_entities[0].name == "mr_fullask" and isinstance(
            user_entities[0], UserModel
        )
        assert user_entities[1].id == 2
        assert user_entities[1].name == "mr_django" and isinstance(
            user_entities[0], UserModel
        )
        assert user_entities[2].id == 3
        assert user_entities[2].name == "mr_fastapi" and isinstance(
            user_entities[0], UserModel
        )


def test_read_by_id_should_return_none(test_app, user_repository):
    """
    If you perform a user lookup with a non-existent ID,
    read_by_id should return None.
    """
    with test_app.test_request_context():
        user = user_repository.read_by_id(1)
    assert user is None


def test_read_by_id_should_return_user_entity(test_app, user_repository):
    """
    If the user information is properly stored in the database table,
    read_by_id should return a UserModel object.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_django"))
        db.session.commit()
        user_fullask = user_repository.read_by_id(1)
        user_django = user_repository.read_by_id(2)
    assert user_fullask.name == "mr_fullask" and isinstance(user_fullask, UserModel)
    assert user_django.name == "mr_django" and isinstance(user_fullask, UserModel)


def test_is_exists_by_id_should_return_false(test_app, user_repository):
    """
    If it can't be found with that ID, it should return False.
    """
    with test_app.test_request_context():
        assert user_repository.is_exists_by_id(1) is False


def test_is_exists_by_id_should_return_true(test_app, user_repository):
    """
    If it can be found by that id, it should return True.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.commit()
        assert user_repository.is_exists_by_id(1) is True


###################
# read_all() TEST #
###################


def test_read_all_return_empty_list(test_app, user_repository):
    """
    If no users are stored in the database, read_all() should return an empty list.
    """
    with test_app.test_request_context():
        read_all_result = user_repository.read_all()
        assert isinstance(read_all_result, list)
        assert len(read_all_result) == 0


def test_read_all_without_sorting_and_filtering_success(test_app, user_repository):
    """
    Test that the read_all() method reads the data well when there are no sorting and filtering request objects.
    If there are two users stored in the database, read_list() should return a list of length 2.
    If no sort request object or filtering object was passed, all data should be returned without pagination,
    in ascending order of ID.
    And each element should be a UserModel object.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_django"))
        db.session.commit()
        read_all_result = user_repository.read_all()
        assert isinstance(read_all_result, list)
        assert len(read_all_result) == 2
        assert read_all_result[0].name == "mr_fullask" and isinstance(
            read_all_result[0], UserModel
        )
        assert read_all_result[1].name == "mr_django" and isinstance(
            read_all_result[1], UserModel
        )


def test_read_all_with_pagination_return_paginated_list(test_app, user_repository):
    """
    Test that the read_all_with_pagination() method reads the data well.
    If you have 5 users stored, paginate 2 of them, and then look up 2 pages, it should perform well.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_django"))
        db.session.add(UserModel(name="mr_spring"))
        db.session.add(UserModel(name="mr_react"))
        db.session.add(UserModel(name="mr_fastapi"))
        db.session.commit()
        read_all_result_with_pagination = user_repository.read_all_with_pagination(
            PaginationRequest(page=2, per_page=2)
        )
        assert isinstance(read_all_result_with_pagination, PaginationResponse)
        assert read_all_result_with_pagination.count == 5
        assert read_all_result_with_pagination.previous_page == 1
        assert read_all_result_with_pagination.next_page == 3
        assert len(read_all_result_with_pagination.results) == 2
        assert read_all_result_with_pagination.results[0].name == "mr_spring"
        assert read_all_result_with_pagination.results[1].name == "mr_react"


def test_read_all_with_pagination_with_sorting_success(test_app, user_repository):
    """
    Test that the read_all_with_pagination() method reads the data well when there is a sorting object.
    If you have 5 users stored, paginate 2 of them, sort them in descending order of ID, and then retrieve 2 pages,
    it should perform well.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_django"))
        db.session.add(UserModel(name="mr_spring"))
        db.session.add(UserModel(name="mr_react"))
        db.session.add(UserModel(name="mr_fastapi"))
        db.session.commit()
        read_all_result_with_pagination = user_repository.read_all_with_pagination(
            PaginationRequest(page=2, per_page=2),
            SortingRequest({"id": "desc"}),
        )

        assert isinstance(read_all_result_with_pagination, PaginationResponse)
        assert read_all_result_with_pagination.count == 5
        assert read_all_result_with_pagination.previous_page == 1
        assert read_all_result_with_pagination.next_page == 3
        assert len(read_all_result_with_pagination.results) == 2
        assert read_all_result_with_pagination.results[0].name == "mr_spring"
        assert read_all_result_with_pagination.results[1].name == "mr_django"


def test_read_all_with_pagination_with_filtering_success(test_app, user_repository):
    """
    Test that the read_all_with_pagination() method reads data well in the presence of a filtering object.
    If you have 5 users stored, paginate 2 of them, and then apply the filter "name contains 'pring',
    If you get 1 page, it should perform well.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_japring"))
        db.session.add(UserModel(name="mr_kopring"))
        db.session.add(UserModel(name="mr_fastapi"))
        db.session.commit()
        read_all_result_with_pagination = user_repository.read_all_with_pagination(
            pagination_request=PaginationRequest(page=1, per_page=2),
            filtering_request=FilteringRequest(name="pring"),
        )

        assert isinstance(read_all_result_with_pagination, PaginationResponse)
        assert (
            read_all_result_with_pagination.count == 2
        )  # filtering result should be 2.
        assert read_all_result_with_pagination.previous_page is None
        assert read_all_result_with_pagination.next_page is None
        assert len(read_all_result_with_pagination.results) == 2  # per_page is 2.
        assert read_all_result_with_pagination.results[0].name == "mr_japring"
        assert read_all_result_with_pagination.results[1].name == "mr_kopring"


def test_read_all_with_pagination_with_filtering_sorting_success(
    test_app, user_repository
):
    """
    Test that the read_all_with_pagination() method reads data well when there is a filtering object
    and a sorting object.
    If you have 5 users stored, paginate 2 of them and then apply the filter "name contains 'pring',
    Sort in reverse order of ID" and retrieve 1 page after the request, it should perform well.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_japring"))
        db.session.add(UserModel(name="mr_kopring"))
        db.session.add(UserModel(name="mr_fastapi"))
        db.session.commit()
        read_all_result_with_pagination = user_repository.read_all_with_pagination(
            pagination_request=PaginationRequest(page=1, per_page=2),
            sorting_request=SortingRequest({"id": "desc"}),
            filtering_request=FilteringRequest(name="pring"),
        )

        assert isinstance(read_all_result_with_pagination, PaginationResponse)
        assert (
            read_all_result_with_pagination.count == 2
        )  # filtering result should be 2.
        assert read_all_result_with_pagination.previous_page is None
        assert read_all_result_with_pagination.next_page is None
        assert len(read_all_result_with_pagination.results) == 2  # per_page is 2.
        assert read_all_result_with_pagination.results[0].name == "mr_kopring"
        assert read_all_result_with_pagination.results[1].name == "mr_japring"


def test_read_all_by_ids(test_app, user_repository):
    """
    Test that the read_all_by_ids() method reads the data well.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))  # id should 1
        db.session.add(UserModel(name="mr_django"))  # id should 2
        db.session.add(UserModel(name="mr_spring"))  # id should 3
        db.session.commit()
        read_all_result = user_repository.read_all_by_ids([1, 3])
        assert isinstance(read_all_result, list)
        assert len(read_all_result) == 2
        assert read_all_result[0].name == "mr_fullask" and isinstance(
            read_all_result[0], UserModel
        )
        assert read_all_result[1].name == "mr_spring" and isinstance(
            read_all_result[1], UserModel
        )


def test_count_should_return_2(test_app, user_repository):
    """
    Test that the count() method returns the correct value.
    If 2 users are stored, the count() method should return 2.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_django"))
        db.session.commit()
        assert user_repository.count() == 2


def test_delete_by_id_should_success(test_app, user_repository):
    """
    Test that the delete_by_id() method does a good job of deleting data by taking an ID.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))  # id should 1
        db.session.add(UserModel(name="mr_django"))  # id should 2
        db.session.commit()
        assert db.session.query(UserModel).count() == 2
        user_repository.delete_by_id(1)
        assert db.session.query(UserModel).count() == 1


def test_delete_by_id_with_unknown_id_should_fail(test_app, user_repository):
    """
    If the delete_by_id() method receives an id, but can't find any data with that id in the database,
    it should raise a ValueError.
    """
    with test_app.test_request_context():
        with pytest.raises(ValueError):
            user_repository.delete_by_id(3)


def test_delete_by_entity_should_success(test_app, user_repository):
    """
    Test that the delete() method takes an entity and deletes the data well.
    If the entity can be found in the database, the deletion should be successful.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))  # id is 1
        db.session.commit()
        assert db.session.query(UserModel).count() == 1
        user = UserModel(id=1, name="mr_fullask")
        user_repository.delete(entity=user)
        assert db.session.query(UserModel).count() == 0


def test_delete_by_invalid_entity_should_fail(test_app, user_repository):
    """
    Test that the delete() method takes an entity and deletes the data well.
    If the entity cannot be found in the database, the delete should fail.
    """
    with test_app.test_request_context():
        # 유효하지 않은 entity 생성
        invalid_user_entity = UserModel(id=2, name="mr_fullask")

        with pytest.raises(ValueError):
            user_repository.delete(invalid_user_entity)


def test_delete_by_valid_entity_should_success(test_app, user_repository):
    """
    Test that the delete() method takes an entity and deletes the data well.
    If the entity can be found in the database, the deletion should be successful.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.commit()
        assert db.session.query(UserModel).count() == 1
        valid_user_entity = UserModel(id=1, name="mr_fullask")
        user_repository.delete(valid_user_entity)
        assert db.session.query(UserModel).count() == 0


def test_delete_all_by_ids_should_success(test_app, user_repository):
    """
    Test that the delete_all_by_ids() method does a good job of deleting data by taking in ids.
    If all the received IDs exist in the database and can be found, the deletion should go well.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))  # id should be 1
        db.session.add(UserModel(name="mr_django"))  # id should be 2
        db.session.add(UserModel(name="mr_fastapi"))  # id should be 3
        db.session.add(UserModel(name="mr_spring"))  # id should be 4
        db.session.commit()

        user_repository.delete_all_by_ids([1, 3, 4])

        assert db.session.query(UserModel).count() == 1


def test_delete_all_should_success(test_app, user_repository):
    """
    Test that the delete_all() method does a good job of deleting data.
    """
    with test_app.test_request_context():
        db.session.add(UserModel(name="mr_fullask"))
        db.session.add(UserModel(name="mr_django"))
        db.session.add(UserModel(name="mr_fastapi"))
        db.session.add(UserModel(name="mr_spring"))
        db.session.commit()

        assert db.session.query(UserModel).count() == 4
        user_repository.delete_all()
        assert db.session.query(UserModel).count() == 0
