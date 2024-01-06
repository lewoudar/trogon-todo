from __future__ import annotations

import copy
from datetime import datetime
from pathlib import Path

import msgspec

from trogon_todo.types import Todo


class TodoError(Exception):
    pass


class TodoNotFoundError(TodoError):
    def __init__(self, todo_id: int):
        self.id = todo_id
        super().__init__(f'No todo found with id {self.id}')


class TodoDAO:
    def __init__(self, db_file: Path):
        self.db = db_file
        self.encoder = msgspec.msgpack.Encoder()
        self.decoder = msgspec.msgpack.Decoder(type=list[Todo])

    def get_todos(self, done: bool | None = None) -> list[Todo]:
        db_content = self.db.read_bytes()
        if not db_content:
            return []

        todos = self.decoder.decode(db_content)
        if done is None:
            return todos
        return [todo for todo in todos if todo.done is done]

    def get_todo(self, todo_id: int, todos: list[Todo] | None = None) -> Todo:
        todos = self.get_todos() if todos is None else todos
        for todo in todos:
            if todo.id == todo_id:
                return todo

        raise TodoNotFoundError(todo_id)

    @staticmethod
    def _next_id(todos: list[Todo]) -> int:
        return todos[-1].id + 1 if todos else 1

    def _save_in_db(self, todos: list[Todo]) -> None:
        self.db.write_bytes(self.encoder.encode(todos))

    def create_todo(self, name: str, description: str | None, due_date: datetime | None) -> Todo:
        todos = self.get_todos()
        todo = Todo(id=self._next_id(todos), name=name, description=description, due_date=due_date)
        todos.append(todo)
        self._save_in_db(todos)
        return todo

    def update_todo(
        self, todo_id: int, name: str | None, description: str | None, due_date: datetime | None, done: bool | None
    ) -> Todo:
        todos = self.get_todos()
        todo = self.get_todo(todo_id, todos)
        new_todo = copy.copy(todo)

        if name is not None:
            new_todo.name = name
        if description is not None:
            new_todo.description = description
        if due_date is not None:
            new_todo.due_date = due_date
        if done is not None:
            new_todo.done = done

        todo_index = todos.index(todo)
        todos.remove(todo)
        todos.insert(todo_index, new_todo)
        self._save_in_db(todos)

        return new_todo

    def delete_todo(self, todo_id: int) -> None:
        todos = self.get_todos()
        todo = self.get_todo(todo_id, todos)
        todos.remove(todo)
        self._save_in_db(todos)

    def clear_db(self) -> None:
        self.db.write_bytes(b'')
