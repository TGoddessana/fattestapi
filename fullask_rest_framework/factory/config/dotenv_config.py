import inspect

from dotenv import load_dotenv


class DotEnvConfig:
    """
    Config class containing the default argumentsto be passed to the load_dotenv() function of the `python-dotenv`.
    Inherit from this class to define new keyword arguments for the load_dotenv file.

    ```
    class MyDotEnvConfig(DotenvConfig):
        dotenv_path = "./foo/bar/.env"
    ```

    flask config is capitalized, so to maintain convention, you can also write it like this

    ```
    class MyDotEnvConfig(DotenvConfig):
        DOTENV_PATH = "./foo/bar/.env"
    ```

    By default, Fullask-REST-Framework will set its class to the default unless there is a custom config.
    """

    def __init__(self):
        dotenv_args = {
            key.upper(): value.default
            for key, value in inspect.signature(load_dotenv).parameters.items()
            if value.default is not inspect.Parameter.empty
        }
        self.__dict__.update(dotenv_args)

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {dict.__repr__(self.__dict__)}>"

    def to_kwargs(self) -> dict:
        return {key.lower(): value for key, value in self.__dict__.items()}
