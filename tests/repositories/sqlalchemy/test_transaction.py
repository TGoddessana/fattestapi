import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from fullask_rest_framework.db.transaction import make_transaction
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
    test_app.config["SQLALCHEMY_ECHO"] = True

    db.init_app(test_app)

    with test_app.app_context():
        UserModel
        db.create_all()

    yield test_app
    with test_app.app_context():
        db.drop_all()


# ##################
# test code starts #
# ##################


def test_transaction_rollback(test_app, user_repository):
    """
    Tests that the make_transaction method handles the transaction correctly.
    If an error occurs in the wrapped method, the session should be rolled back.
    """
    with test_app.test_request_context():
        user_fullask = UserModel(name="mr_fullask")
        user_spring = UserModel(name="mr_spring")
        with pytest.raises(Exception):

            def raise_exception():
                return 1 / 0

            @make_transaction
            def save_user():
                user_repository.save(user_fullask)
                user_repository.save(user_spring)
                raise_exception()

            save_user()
    with test_app.test_request_context():
        assert UserModel.query.count() == 0


def test_transaction_success(test_app, user_repository):
    """
    Test that the make_transaction method handles the transaction well.
    If the wrapped method doesn't throw any errors, the database should have two users successfully committed.
    """
    with test_app.test_request_context():
        user_fullask = UserModel(name="mr_fullask")
        user_spring = UserModel(name="mr_spring")

        @make_transaction
        def save_user():
            user_repository.save(user_fullask)
            user_repository.save(user_spring)

        save_user()
    with test_app.test_request_context():
        assert UserModel.query.count() == 2


def test_without_decorator(test_app, user_repository):
    """
    Without the make_transaction decorator, no changes will be made to the actual database,
    so the user should remain unsaved.
    """
    with test_app.test_request_context():
        user_fullask = UserModel(name="mr_fullask")
        user_spring = UserModel(name="mr_spring")
        with pytest.raises(Exception):

            def raise_exception():
                return 1 / 0

            def save_user():
                user_repository.save(user_fullask)
                user_repository.save(user_spring)
                raise_exception()

            save_user()
    with test_app.test_request_context():
        assert UserModel.query.count() == 0
