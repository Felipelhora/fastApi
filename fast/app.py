
from http import HTTPStatus

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from fast.schemas import Message


app = FastAPI()



### Status code é o Status que espera de resposta padrão, neste caso é usado o HTTPStatus para trocar número por STRINHG
### response_model - Vincula o schema para indicar o tipo de resposta e como é a estrutura inclusive na documentação, e só retorna o que 
### está no contrato, neste caso se houver outro elemento que não esteja no contrato ele não retorna, e se faltar da erro (DTO)
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "ola mundo", "teste":"foi"}

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

