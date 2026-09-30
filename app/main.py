from fastapi import FastAPI

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