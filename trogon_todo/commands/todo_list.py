from typing import TYPE_CHECKING

import click
from rich.table import Table

from trogon_todo.console import console
from trogon_todo.options import get_done_argument
from trogon_todo.types import Todo

if TYPE_CHECKING:
    from trogon_todo.main import Container


def print_table(todos: list[Todo]) -> None:
    table = Table(title='Todos', header_style='bold magenta')
    for item in ['ID', 'Name', 'Description', 'Done', 'Due date']:
        table.add_column(item)

    for todo in todos:
        table.add_row(*todo.row())

    console.print(table)


@click.command('list')
@click.option('--done', is_flag=True, help='Filter to select done todos.')
@click.option('--not-done', is_flag=True, help='Filter to select not done todos.')
@click.pass_obj
def todo_list(obj: 'Container', done: bool, not_done: bool):
    """List todos."""
    done = get_done_argument(done, not_done)
    print_table(obj.dao.get_todos(done=done))
