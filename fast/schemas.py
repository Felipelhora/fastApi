from pydantic import BaseModel


class Message(BaseModel): # A função dos squemas é dizer na documentação que tipo de de retorno será feito
    message: str
