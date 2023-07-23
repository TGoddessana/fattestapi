import importlib
import inspect
import pathlib
import pkgutil
import typing as t
import uuid

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer, DynamicContainer
from dependency_injector.wiring import Provide, inject
from flask import Blueprint, Flask
from werkzeug.exceptions import HTTPException

from fattestapi.factory.exceptions import ConfigNotSetError, ExtensionError
from fattestapi.factory.extensions import (
    cors,
    db,
    jwt,
    ma,
    migrate,
    smorest,
)


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
    A Factory class for building Flask applications.
    """

    # The top-level directory of the application.
    BASE_DIR = pathlib.Path(__file__).parent.parent

    # Sometimes you may need to use your own customized classes, rather than the Flask class provided by Flask.
    # If you do, set the `CLASK_CLS` variable to the desired Flask wrapper class or something.
    # The corresponding Factory class will then build your Flask application, based on the provided class.
    FLASK_CLS: type[Flask] = Flask

    # Define the parameters that go into `__init__()` method, of `Flask`.
    # See more info in `https://flask.palletsprojects.com/en/2.3.x/api/# flask.Flask`.
    FLASK_KWARGS: t.Dict = {
        "import_name": __qualname__,
    }

    # Put a Flask extension objects that support `init_app()` methods.
    EXTENSIONS: t.Sequence = [
        smorest,
        db,
        cors,
        ma,
        jwt,
        migrate,
    ]

    # You can separate environments in a dictionary format.
    CONFIG_MAPPING: t.Dict[str, Config] = {
        "default": Config,
    }

    # Define route mappings.
    # You can register parameters in the form {url_prefix, Blueprint object, or module name containing the Blueprint}
    # that will go into the Flask app's register_blueprint().
    ROUTE_MAPPING: t.Dict[str, t.Union[Blueprint, str]] = {}

    # Register a non-standard HTTP Status code.
    # The class being registered must be a subclass of werkzeug.exceptions.HTTPExceptions.
    CUSTOM_HTTP_ERRORS: t.List[HTTPException] = []

    # Register an error handler function for the expected HTTP code.
    ERROR_HANDLERS: t.Dict[t.Union[HTTPException, int], t.Callable] = {}

    # Register the required Flask middleware. Note that this must not be WSGI Middleware.
    MIDDLEWARES: t.Dict[str, t.List[t.Callable]] = {
        "BEFORE_REQUEST": [],
        "AFTER_REQUEST": [],
        "TEARDOWN_REQUEST": [],
        "TEARDOWN_APPCONTEXT": [],
    }

    DI_CONTAINERS: t.Sequence[t.Type[DeclarativeContainer | DynamicContainer]] = [
        Container,
        Container2,
    ]

    def create_app(self, environment: str) -> Flask:
        """
        Builds a Flask application based on your settings.

        :param environment:
            A key in `CONFIG_MAPPING` dictionary. this will create a Flask application by injecting
            the environment that matches the key.
        """
        _app = self._create_flask()
        self._load_config(_app=_app, environment=environment)
        self._load_extensions(_app=_app)
        self._register_custom_http_errors(_app=_app)
        self._register_error_handlers(_app=_app)
        # self._register_jwt_handlers(_app=_app)
        self._load_middlewares(_app=_app)
        self._route(_app=_app)
        self._setup_di(_app=_app)
        return _app

    def _create_flask(self) -> Flask:
        """
        Create a flask application for a given flask, or a custom flask wrapper class.
        By defining `FLASK_KWARGS`, you can define the parameters that will be passed to `Flask.__init__()`.
        """
        return self.FLASK_CLS(**self.FLASK_KWARGS)

    def _load_config(self, _app: Flask, environment: str) -> None:
        """
        Load Flask Config according to your customization mapping.

        :param environment: the key of your `CONFIG_MAPPING`.
        """
        try:
            return _app.config.from_object(self.CONFIG_MAPPING[environment])
        except KeyError:
            raise ConfigNotSetError(
                f"Environment '{environment}' is not set in the CONFIG_MAPPING."
                f"available environments are: {list(self.CONFIG_MAPPING.keys())}"
            )

    def _load_extensions(self, _app: Flask) -> None:
        """
        Load the Flask extensions in the `EXTENSIONS` list.
        Make sure that each extension object supports `init_app(app)` style initialization.
        """
        for extension in self.EXTENSIONS:
            try:
                extension.init_app(app=_app)
            except AttributeError:
                raise ExtensionError(
                    f"The extension object {extension} does not support "
                    f"the init_app() method of initialization."
                )

    def _register_custom_http_errors(self, _app: Flask) -> None:
        """
        Registers user-specific HTTP errors that are registered in `CUSTOM_ERRORS`.
        Make sure that each element is a subclass of `werkzeug.exceptions.HTTPExceptions`.

        This makes it possible to abort() for non-standard HTTP status codes registered later.
        """
        for error in self.CUSTOM_HTTP_ERRORS:
            _app.aborter.mapping.update({error.code: error})

    def _register_error_handlers(self, _app: Flask) -> None:
        """
        Register an error handler function for the expected HTTP code.
        """
        for exc, handler_func in self.ERROR_HANDLERS.items():
            _app.register_error_handler(exc, handler_func)

    def _load_middlewares(self, _app: Flask) -> None:
        """
        load flask middlewares, that are registered in `MIDDLEWARES`.
        """
        for method, middlewares in self.MIDDLEWARES.items():
            for middleware in middlewares:
                getattr(_app, method.lower())(middleware)

    def _route(self, _app: Flask) -> None:
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

    def _setup_di(self, _app: Flask) -> None:
        """
        Setup DI Container.
        """
        for _Container in self.DI_CONTAINERS:
            setattr(_app, _Container.__name__.lower(), _Container())
            print(_Container().__dict__["providers"])


if __name__ == "__main__":
    fa = Factory()
    app = fa.create_app(environment="default")
    app.run()
