from fastapi import FastAPI
from src.database import db_client
from src.controllers import post, auth
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
app.include_router(auth.router)
