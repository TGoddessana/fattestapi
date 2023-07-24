import importlib
import inspect
import pathlib
import typing as t

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, DynamicContainer
from fastapi import FastAPI


class Config:
    API_TITLE = ""
    API_VERSION = ""
    OPENAPI_VERSION = "3.0.0"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class Container(DeclarativeContainer):
    string1 = providers.Factory(Config)


class Container2(DeclarativeContainer):
    string2 = providers.Factory(Config)


class Factory:
    """
    A Factory class for building FastAPI applications.
    """

    # The top-level directory of the application.
    BASE_DIR = pathlib.Path(__file__).parent.parent

    # Sometimes you may need to use your own customized classes, rather than the FastAPI class provided by FastAPI.
    # If you do, set the `FASTAPI_CLS` variable to the desired FastAPI wrapper class or something.
    # The corresponding Factory class will then build your FastAPI application, based on the provided class.
    FASTAPI_CLS: type[FastAPI] = FastAPI

    DI_CONTAINERS: t.Sequence[t.Type[DeclarativeContainer | DynamicContainer]] = [
        Container,
        Container2,
    ]

    def create_app(self, environment: str) -> FastAPI:
        """
        Builds a FastAPI application based on your settings.

        :param environment:
            A key in `CONFIG_MAPPING` dictionary. this will create a FastAPI application by injecting
            the environment that matches the key.
        """
        _app = self._create_fastapi()
        return _app

    def _create_fastapi(self) -> FastAPI:
        """
        Create a FastAPI application for a given FastAPI, or a custom FastAPI wrapper class.
        By defining `FastAPI_KWARGS`, you can define the parameters that will be passed to `FastAPI.__init__()`.
        """
        return self.FASTAPI_CLS()

    # def _load_config(self, _app: FastAPI, environment: str) -> None:
    #     """
    #     Load FastAPI Config according to your customization mapping.
    #
    #     :param environment: the key of your `CONFIG_MAPPING`.
    #     """
    #     try:
    #         return _app.config.from_object(self.CONFIG_MAPPING[environment])
    #     except KeyError:
    #         raise ConfigNotSetError(
    #             f"Environment '{environment}' is not set in the CONFIG_MAPPING."
    #             f"available environments are: {list(self.CONFIG_MAPPING.keys())}"
    #         )

    def _route(self, _app: FastAPI) -> None:
        """
        Register blueprints.
        """
        for url_prefix, blueprint in self.ROUTE_MAPPING.items():
            try:
                _app.register_blueprint(url_prefix=url_prefix, blueprint=blueprint)
            except AttributeError:
                blueprints = [
                    obj
                    for name, obj in inspect.getmembers(
                        importlib.import_module(blueprint)
                    )
                    if isinstance(obj, Blueprint)
                ]
                for blp in blueprints:
                    _app.register_blueprint(url_prefix=url_prefix, blueprint=blp)


fa = Factory()
app = fa.create_app(environment="default")

