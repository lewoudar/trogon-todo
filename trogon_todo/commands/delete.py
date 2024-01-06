from __future__ import annotations

from typing import TYPE_CHECKING

import click

from trogon_todo.console import console
from trogon_todo.db import TodoNotFoundError

if TYPE_CHECKING:
    from trogon_todo.main import Container


@click.command()
@click.option('-i', '--id', 'todo_ids', type=int, multiple=True, help='IDs of todos to be deleted.')
@click.pass_obj
def delete(obj: Container, todo_ids: list[int]):
    """
    Delete todos given their IDs.

    Example usage:

    # delete one todo
    $ todo delete -i 1

    # delete many todos
    $ todo delete -i 1 -i 2
    """
    if not todo_ids:
        console.print('[info]No IDs provided.')
        return

    ids_not_found = []
    ids_found = []
    for todo_id in todo_ids:
        try:
            obj.dao.delete_todo(todo_id)
            ids_found.append(todo_id)
        except TodoNotFoundError:
            ids_not_found.append(todo_id)

    if ids_not_found:
        console.print(f'[warning]The following IDs were not found: {", ".join(map(str, ids_not_found))}')

    if ids_found:
        console.print(f'[success]Successfully deleted todos with IDs: {", ".join(map(str, ids_found))} :partying_face:')
