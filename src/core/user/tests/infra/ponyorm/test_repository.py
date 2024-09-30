import uuid

import pytest
from pony.orm import db_session, rollback

from src.core.user.domain.repository.user_repository import UserInput
from src.core.user.infra.ponyorm.models.user import db
from src.core.user.infra.ponyorm.repository.user_repository import PonyORMUserRepository


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    db.bind(provider='sqlite', filename=':memory:', create_db=True)
    db.generate_mapping(create_tables=True)
    yield
    db.disconnect()

@pytest.fixture(scope="function", autouse=True)
def db_session_fixture():
    with db_session:
        yield
        rollback()
        
@pytest.mark.asyncio
async def test_save():
    repository = PonyORMUserRepository()
    user_input = UserInput(id=uuid.uuid4(), email="test@example.com", password="password123")

    user_output = await repository.save(user_input)
    
    assert user_output.email == user_input.email
    assert user_output.password == user_input.password
    assert user_output.id == user_input.id
    

    
    saved_user = await repository.get_by_email(user_input.email)
    
    assert saved_user is not None
    assert saved_user.email == user_input.email
    assert saved_user.password == user_input.password
    assert saved_user.id == user_input.id

    await repository.clear()

