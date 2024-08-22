import pytest
from fastapi.testclient import TestClient

from fast.app import app


@pytest.fixture
def client():
    return TestClient(app)




### o arquivo deve exatamente este nome conftest.py, ele será importado automaticamente pelos testes, e o client estará visível para ser usado nos testes
