from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import run_agent

app = FastAPI(title="AutoStream AI Agent")

class Query(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "AutoStream API running"}

@app.post("/chat")
def chat(query: Query):
    response = run_agent(query.message)
    return {"response": response}
