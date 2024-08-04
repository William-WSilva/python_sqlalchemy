from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# conectar ao sqlite me memoria
engine = create_engine('sqlite:///meubanco.db', echo=True)
print('Conexão com SQlite estabelecida')

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar tabelas no banco
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Gerenciador de contexto, Comits, Rollbacks e etc
with Session () as session:
    novo_usuario = Usuario(nome='Ana', idade=30)
    session.add(novo_usuario)
    session.commit()

usuario = session.query(Usuario).filter_by(nome='Ana').first()
print(f'Usuario encontrado: {usuario.nome}, Idade {usuario.idade}')


