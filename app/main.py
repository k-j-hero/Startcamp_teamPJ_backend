from fastapi import FastAPI

app = FastAPI(title="My FastAPI")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}