from fastapi import FastAPI
from routes.index import user

app = FastAPI(title="OPERATION CRUD AVEC FASTAPI", version="KKY")

app.include_router(user)