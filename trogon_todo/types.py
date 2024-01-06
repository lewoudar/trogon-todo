from __future__ import annotations

from datetime import datetime
from typing import Any

import msgspec


class Todo(msgspec.Struct):
    id: int
    name: str
    description: str | None = None
    done: bool = False
    due_date: datetime | None = None

    def dict(self) -> dict[str, Any]:
        result = msgspec.structs.asdict(self)
        result['due_date'] = self.due_date.isoformat() if self.due_date is not None else None
        return result

    def row(self) -> list:
        result = []
        for key, value in msgspec.structs.asdict(self).items():
            if key == 'done':
                result.append('Yes' if value else 'No')
            elif key == 'due_date':
                result.append(value.isoformat() if value is not None else '')
            else:
                result.append(str(value) if value else '')
        return result
