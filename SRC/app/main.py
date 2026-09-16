from fastapi import FastAPI

app = FastAPI(
    title="DocKeep",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome To DocKeep"}