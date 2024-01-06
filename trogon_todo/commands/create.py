from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import click

from trogon_todo.console import console

if TYPE_CHECKING:
    from trogon_todo.main import Container


@click.command()
@click.option('-n', '--name', prompt='Todo name', help='The name of the todo.')
@click.option('-d', '--description', help='The description of the todo.')
@click.option('-D', '--due-date', help='The todo due date.', type=click.DateTime())
@click.pass_obj
def create(obj: Container, name: str, description: str | None, due_date: datetime | None):
    """
    Creates a todo.

    Example usage:

    \b
    # create a todo
    $ todo create --name=foo

    \b
    # create a todo with additional metadata
    $ todo create --name=foo --description=bar --due-date="2024-01-01"

    \b
    # create a todo with more precise due date
    $ todo create -n foo -D "2024-01-01 12:10:00"
    """
    todo = obj.dao.create_todo(name, description, due_date)
    console.print_json(data=todo.dict())
    console.print(f'[success]Todo [italic bold]{todo.name}[/] was created and saved! :partying_face:')
