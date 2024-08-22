from http import HTTPStatus


def test_read_root_deve_retornar_ok(client):
    # client  = TestClient(app) # arrumar
    response = client.get('/') # teste em si action
    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == 'teste'


# def teste_create_user_deve_retornar_201(client):
#     # client  = TestClient(app)
#     response =  client.post('/users', json={'username':'testename', 'password': 'password', "email": "teste@teste.com"})
#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json == {
#                                     {'username':'testename', 'id': 1, "email": "teste@teste.com"}
#                             }
