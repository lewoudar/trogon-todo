from typing import TYPE_CHECKING

import click

from trogon_todo.console import console

if TYPE_CHECKING:
    from trogon_todo.main import Container


@click.command('clear-db')
@click.pass_obj
def clear_db(obj: 'Container'):
    """Clear the database."""
    obj.dao.clear_db()
    console.print('[info]Database cleared.')
