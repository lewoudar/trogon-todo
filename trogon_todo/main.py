import click
import platformdirs
from click_didyoumean import DYMGroup
from trogon import tui

from trogon_todo.commands.clear_db import clear_db
from trogon_todo.commands.completion import install_completion
from trogon_todo.commands.create import create
from trogon_todo.commands.delete import delete
from trogon_todo.commands.get import get
from trogon_todo.commands.todo_list import todo_list
from trogon_todo.commands.update import update
from trogon_todo.db import TodoDAO


class Container:
    def __init__(self):
        self.todo_data_dir = platformdirs.user_data_path(appname='todo')
        self.todo_db = self.todo_data_dir / 'todo.db'
        if not self.todo_data_dir.exists():
            self.todo_data_dir.mkdir(parents=True, exist_ok=True)
            self.todo_db.touch()

        self.dao = TodoDAO(self.todo_db)


@tui()
@click.version_option('0.1.0', message='%(prog)s version %(version)s')
@click.group(cls=DYMGroup, context_settings={'help_option_names': ['-h', '--help']})
@click.pass_context
def cli(context):
    """
    A simple command line to handle your todo list.

    Example usage:

    \b
    # create a todo
    $ todo create --name=foo

    \b
    # create a todo with additional metadata
    $ todo create --name=foo --description=bar --due-date="2024-01-01"

    \b
    # get a todo
    $ todo get --id=1

    \b
    # list todos
    $ todo list

    \b
    # update a todo
    $ todo update --id=1 --name=foobar --description=hell --due-date="2024-01-02"

    \b
    # mark a todo as done
    $ todo update --id=1 --done

    \b
    # mark a todo as not done
    $ todo update --id=1 --not-done

    \b
    # delete todos
    $ todo delete --id=1 --id=2

    \b
    # delete all todos
    $ todo clear-db
    """
    context.obj = Container()


for command in [todo_list, create, clear_db, get, update, delete, install_completion]:
    cli.add_command(command)
