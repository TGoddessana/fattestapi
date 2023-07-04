import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from fullask_rest_framework.httptypes import (
    FilteringRequest,
    PaginationRequest,
    PaginationResponse,
    SortingRequest,
)
from fullask_rest_framework.repositories.sqlalchemy.sqlalchemy import (
    SQLAlchemyFullRepository,
)

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


##############
# read_by_id #
##############


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


###################
# is_exists_by_id #
###################


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


############
# read_all #
############


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
    If there are two users stored in the database, read_all() should return a list of length 2.
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
        read_all_result_with_pagination = user_repository.read_all(
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
        read_all_result_with_pagination = user_repository.read_all(
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
        read_all_result_with_pagination = user_repository.read_all(
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
        read_all_result_with_pagination = user_repository.read_all(
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


#########
# count #
#########


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
