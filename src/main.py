from fastapi import FastAPI
from src.controllers import post, auth


app = FastAPI()
app.include_router(post.router)
app.include_router(auth.router)
