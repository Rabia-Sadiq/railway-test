from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from Railway", "status": "ok"}


@app.get("/health")
def health():
    return {"healthy": True}