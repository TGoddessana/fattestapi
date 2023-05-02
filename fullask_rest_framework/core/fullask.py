from flask import Flask, cli

from fullask_rest_framework.cli import show_server_banner


class Fullask(Flask):
    def __init__(self, import_name: str):
        super().__init__(import_name)
        cli.show_server_banner = show_server_banner


def create_app() -> Fullask:
    return Fullask("simple app")


app = create_app()

app.run()
