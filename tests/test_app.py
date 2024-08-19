from http import HTTPStatus

from fastapi.testclient import TestClient

from fast.app import app


def test_read_root_deve_retornar_ok():
    client  = TestClient(app) # arrumar
    response = client.get('/') # teste em si action
    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == 'teste'
