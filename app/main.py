from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

app.title = "API NFL"

@app.get("/")
async def root():
    return {"message": "Welcome to the NFL API"}
