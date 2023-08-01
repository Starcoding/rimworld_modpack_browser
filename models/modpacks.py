from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class ModPacks(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # in_user_favourite_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    short_description: Mapped[str | None]
    description: Mapped[str | None]
    logo: Mapped[str | None]
    save_file: Mapped[str | None]
    mod_string: Mapped[str | None]
    images: Mapped[str | None]
    seen_counter: Mapped[int] = mapped_column(default=0)

    author: Mapped["Users"] = relationship(back_populates="modpacks_author")
    # in_user_favourite: Mapped["Users.favourite_modpacks"] = relationship(back_populates="favourite_modpacks")
