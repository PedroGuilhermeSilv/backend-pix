from src.db.config import db
from src.core.user.infra.ponyorm.models.user import User  # noqa

db.bind(provider='sqlite', filename='database.db', create_db=True)
db.generate_mapping(create_tables=True)