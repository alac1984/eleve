from typing import Optional

from sqlmodel import SQLModel, Field


class Task(SQLModel, table=True):
    oid: Optional[int] = Field(default=None, primary_key=True)
    name: str
