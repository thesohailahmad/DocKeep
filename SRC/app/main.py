from fastapi import FastAPI, Depends , HTTPException
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DocKeep",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Welcome To DocKeep"}