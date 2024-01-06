# Trogon todo

A toy project to illustrate this blog post. It is a command line interface to handle your daily todos.
It comes with a textual user interface powered by Trogon.

## Installation

To use it, you will need **Python 3.8** or higher. If this prerequisite is OK, you can run one the following
commands:

```shell
# with pip
$ pip install git+https://github.com/lewoudar/trogon_todo

# with poetry
$ poetry add git+https://github.com/lewoudar/trogon_todo

# with pipx
$ pipx install git+https://github.com/lewoudar/trogon_todo
```

## Usage

Hopefully, you will understand how to use it just by reading the command documentation :)

```shell
$ todo --help
Usage: todo [OPTIONS] COMMAND [ARGS]...

  A simple command line to handle your todo list.

  Example usage:

  # create a todo
  $ todo create --name=foo

  # create a todo with additional metadata
  $ todo create --name=foo --description=bar --due-date="2024-01-01"

  # get a todo
  $ todo get --id=1

  # list todos
  $ todo list

  # update a todo
  $ todo update --id=1 --name=foobar --description=hell --due-date="2024-01-02"

  # mark a todo as done
  $ todo update --id=1 --done

  # mark a todo as not done
  $ todo update --id=1 --not-done

  # delete todos
  $ todo delete --id=1 --id=2

  # delete all todos
  $ todo clear-db

Options:
  --help  Show this message and exit.

Commands:
  clear-db  Clear the database.
  create    Creates a todo.
  delete    Delete todos given their IDs.
  get       Gets todo information by its id.
  list      List todos.
  update    Updates a todo.
```

And if it is still not clear, you can use this command to guide you.

```shell
$ todo tui
```