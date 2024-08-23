from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

# registra metadados das tabelas
table_registry = registry()

## classe de dados
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    # init False é pq o Banco dados que irá atribuir e não serpa enviado pelo usuario
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email : Mapped[str] = mapped_column(unique=True)
    # server_defaault é para indicar que o valor virá de uma função do servidor
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
