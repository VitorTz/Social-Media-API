from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Post(BaseModel):

    user_id: int
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
  
  
@app.post("/posts")
async def create_post(payload: Post):
    pass


@app.get("/posts")
def get_posts(payload):
    pass


@app.get("/posts/{id}")
def get_posts_by_id(payload):
    pass


@app.put("/posts/{id}")
def update_post(payload):
    pass


@app.delete("/posts/{id}")
def delete_post(payload):
    pass