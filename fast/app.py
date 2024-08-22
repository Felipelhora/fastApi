
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast.schemas import Message, UserPublic, UserSchema, UserList

app = FastAPI()



database = {
            "username": "felipe",
            "password": "1231",
            "email": "asdad@asdad.com",
            "id": "1"
            }



### Status code é o Status que espera de resposta padrão, neste caso é usado o HTTPStatus para trocar número por STRINHG
### response_model - Vincula o schema para indicar o tipo de resposta e como é a estrutura inclusive na documentação, e só retorna o que
### está no contrato, neste caso se houver outro elemento que não esteja no contrato ele não retorna, e se faltar da erro (DTO)
@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {"message": "ola mundo", "teste":"foi"}



## response_class é para indicar que tipo de resposta será (json ou html) o padrão é json
@app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():
    return '''
                <html>
                <body>
	                TESTE
	                <script type="text/javascript">
		            </script>

                </body>
                </html>
            '''

# status code padrão é 200 (OK)
@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user:UserSchema):
    return database




@app.get('/users', status_code=HTTPStatus.OK, response_model=UserPublic)
def get_user():
    return database



@app.put('/users/{user_id}',  status_code=HTTPStatus.OK, response_model=UserPublic)
# a validação de entrada da função pode ser um esquema pre feito ou um tipo predefinido, na verdade os schemas são abstrações para facilitar apenas a entrada
# da função, ou seja, os itens descritos na schema poderia ser colocados como o user_id abaixo:
#validação de entrada é dentro dos parametros da função, parametros de saída é o response_model
def update_user(user_id:int):
    return database
