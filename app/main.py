from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Kubesentinel")

@app.get("/")
def root():
    return {
        "service": "Kubesentinel",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

Instrumentator().instrument(app).expose(app)
