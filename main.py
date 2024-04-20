from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Post(BaseModel):

    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to my API"}


@app.get("/posts/postid")
def get_posts():
    return {"data": "This is your post"}


@app.post("/posts")
def post(payload: Post):
    return {
        "data": payload.dict()        
    }