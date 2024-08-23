from pydantic import BaseModel, EmailStr


class Message(
    BaseModel
):  # A função dos squemas é dizer na documentação que tipo de de retorno será feito
    message: str


# Modelo de contrato de entrada
class UserSchema(BaseModel):
    username: str
    email: EmailStr | None
    password: str


# Modelo de contrato de saída
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    user: list[UserPublic]
