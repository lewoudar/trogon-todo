from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import click

from trogon_todo.console import console
from trogon_todo.options import get_done_argument

if TYPE_CHECKING:
    from trogon_todo.main import Container


@click.command()
@click.option('-i', '--id', 'todo_id', required=True, type=int, help='The ID of the todo.')
@click.option('-n', '--name', help='The new name of the todo.')
@click.option('-d', '--description', help='The new description of the todo.')
@click.option('-D', '--due-date', type=click.DateTime(), help='The new due date of the todo.')
@click.option('--done', is_flag=True, help='Mark the todo as done.')
@click.option('--not-done', is_flag=True, help='Mark the todo as not done.')
@click.pass_obj
def update(
    obj: Container,
    todo_id: int,
    name: str | None,
    description: str | None,
    due_date: datetime | None,
    done: bool,
    not_done: bool,
):
    """
    Updates a todo.

    Example usage:

    \b
    # update a todo
    $ todo update --id=1 --name=foobar --description=hell --due-date="2024-01-02"

    \b
    # mark a todo as done
    $ todo update --id=1 --done

    \b
    # mark a todo as not done
    $ todo update --id=1 --not-done
    """
    done = get_done_argument(done, not_done)
    todo = obj.dao.update_todo(todo_id, name, description, due_date, done)
    console.print_json(data=todo.dict())
    console.print(f'[success]Todo [italic bold]{todo.name}[/] was updated and saved! :partying_face:')
