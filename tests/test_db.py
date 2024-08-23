from sqlalchemy import select

from fast.models import User


def test_create_users(session):
    # conexão com o banco | memory em memoria volatil ele abre quando termian ele deleta
    '''engine = create_engine('sqlite:///:memory:') #-> migrado para conftest.py'''
    # recolhe todos os metadados das tabelas para criar o as tabelas
    '''table_registry.metadata.create_all(engine) #-> migrado para conftest.py'''
    # A session prepara tudo para ser salvo colocando em "memória" os dados antes executar
    # no banco
    ''' with Session(engine) as session: #-> migrado para conftest.py'''
    user = User(username="user", password="pass", email="email@teste.com")
    # coloca os dados do usuario "temporariamente na memoria"
    session.add(user)
    # o commit é usado para executar a ação no banco dos dados temporários
    session.commit()
    # sincroniza d dado user com o do banco trazendo os ID e os demais campos
    ### OPAÇÂO
    '''session.refresh(user)'''
    # ou pode ser feito
    result = session.scalar(
                select(User).where(User.email == "email@teste.com")
                            )

    assert result.username == "user"
