import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast.app import app
from fast.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


### o arquivo deve exatamente
### este nome conftest.py, ele será importado automaticamente pelos testes,
### e o client estará visível para ser usado nos testes

### a fixture é feita como abstração para ser usado em outros arquivos para não
### ter que ficar repetindo
@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    table_registry.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
