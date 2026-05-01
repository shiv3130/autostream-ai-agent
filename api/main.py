from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from src.agent import run_agent
import time

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now (later restrict)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str


def stream_response(text):
    words = text.split()
    for word in words:
        yield word + " "
        time.sleep(0.03)  # simulate streaming


@app.post("/chat")
def chat(query: Query):
    full_response = run_agent(query.message)

    return StreamingResponse(
        stream_response(full_response),
        media_type="text/plain"
    )
