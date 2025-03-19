from fastapi import FastAPI, HTTPException
from app.database import SessionLocal, engine
from app.agents import run_agents
from app.models import Base, Cliente
import uuid

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/buscar")
def buscar_cliente(nome: str, telefone: str):
    session = SessionLocal()
    
    cliente = session.query(Cliente).filter_by(nome=nome, telefone=telefone).first()
    if cliente:
        return cliente.to_dict()
    
    result = run_agents(nome, telefone)

    if not result:
        raise HTTPException(status_code=404, detail="Nenhuma informação encontrada")
    
    novo_cliente = Cliente(id=str(uuid.uuid4()), **result)
    session.add(novo_cliente)
    session.commit()

    return result