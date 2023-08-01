from typing import List
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class Users(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    uuid: Mapped[UUID | None]
    nickname: Mapped[str]
    modpacks_author: Mapped[List["ModPacks"]] = relationship(back_populates="author")
    # favourite_modpacks: Mapped[List["ModPacks"]] = relationship(back_populates="in_user_favourite")
