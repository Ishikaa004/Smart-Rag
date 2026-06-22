from fastapi import FastAPI
from backend.services.rag_pipeline import ingest_document, query_rag


app=FastAPI(
    title="SMART RAG"
)

@app.post("/ingest")
def ingest(text: str):
    return ingest_document(text) 

@app.get("/query")
def query(q: str):
    return query_rag(q)

@app.get("/")
def message():
    return {"message": "Smart RAG backend is running"}