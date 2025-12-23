from fastapi import FastAPI
from src.database import db_client, metadata, engine
from src.controllers import post, auth
from contextlib import asynccontextmanager


app = FastAPI()
app.include_router(post.router)
app.include_router(auth.router)
