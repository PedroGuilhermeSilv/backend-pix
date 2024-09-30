from uuid import UUID

from pony.orm import Optional, PrimaryKey

from src.db.config import db


class User(db.Entity):
    id = PrimaryKey(UUID, auto=True)
    email = Optional(str)
    password = Optional(str)




