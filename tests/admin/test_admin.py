import pytest
from flask import url_for

from fullask_rest_framework.factory.app_factory import BaseApplicationFactory


@pytest.fixture()
def test_app():
    class TestConfig:
        API_TITLE = "Crescendo_backend Server API"
        API_VERSION = "v1"
        OPENAPI_VERSION = "3.0.0"
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    class TestApplicationFactory(BaseApplicationFactory):
        APP_BASE_DIR = None
        CONFIG_MAPPING = {
            "test": {
                "from_object": (TestConfig(),),
            },
        }
        EXTENSION_MODULE = "fullask_rest_framework.factory.extensions"
        MICRO_APP_CONFIG = None

    yield TestApplicationFactory.create_app("test")


def test_admin_index_page_loads(test_app):
    with test_app.test_request_context():
        response = test_app.test_client().get(url_for("AdminPage.admin_index"))
