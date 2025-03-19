from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False, unique=True)
    cpf = Column(String)
    localizacao = Column(String)
    profissao = Column(String)

    def to_dict(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "cpf": self.cpf,
            "localizacao": self.localizacao,
            "profissao": self.profissao
        }