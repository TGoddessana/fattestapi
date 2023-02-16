import os
from pathlib import Path
from jinja2 import Template

import click

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def create_file_from_template(project_path: Path, template_file: Path, **kwargs):
    """make .fullasktemplate file to .py file."""
    result_filename = ".".join(os.path.basename(template_file).split(".")[:2])
    with open(os.path.join(project_path, result_filename), "w") as f:
        f.write(Template(open(template_file).read()).render(**kwargs))


@click.group
def main():
    pass


@main.command("createproject")
@click.argument("project_name", type=click.STRING, required=True)
@click.argument("path", type=click.Path(exists=True), default=".", required=True)
def create_project(project_name: str, path: str) -> None:
    """Create a new Project Files at this given path and project name."""
    project_template_path = Path(
        os.path.abspath(
            os.path.join(
                ROOT_DIR, "architecture_template/project_template/{{ project_name }}"
            )
        )
    )
    path_by_user: Path = Path(os.path.abspath(os.path.join(Path.cwd(), path)))
    if Path(path).is_dir():
        project_path = Path(os.path.join(path_by_user, project_name))
        project_path.mkdir()
        for template_file in project_template_path.iterdir():
            create_file_from_template(
                project_path=project_path,
                template_file=template_file,
                project_name=project_name,
            )
    else:
        raise click.BadParameter(
            f"{path_by_user} is a file, not directory.",
            param_hint="[PATH]",
        )


if __name__ == "__main__":
    main()
