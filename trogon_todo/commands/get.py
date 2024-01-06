from __future__ import annotations

from typing import TYPE_CHECKING

import click

from trogon_todo.console import console
from trogon_todo.db import TodoNotFoundError

if TYPE_CHECKING:
    from trogon_todo.main import Container


@click.command()
@click.option('-i', '--id', 'todo_id', prompt='Todo ID', type=int, help='The ID of the todo.')
@click.pass_obj
def get(obj: Container, todo_id: int):
    """
    Gets todo information by its id.

    Example usage:

    $ todo get -i 1
    """
    try:
        todo = obj.dao.get_todo(todo_id)
        console.print_json(data=todo.dict())
    except TodoNotFoundError:
        console.print(f'[error]No todo found with id [italic bold]{todo_id}[/]')
        raise SystemExit(1) from None
