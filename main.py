from fastapi import FastAPI, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


my_posts: dict = {

}


class Post(BaseModel):

    user_id: int
    title: str
    content: str
    published: Optional[bool] = True
    rating: Optional[int] = None


@app.get("/")
def home():
    return {"message": "Hello, World!"}
  
@app.post("/posts")
def create_pos(post: Post):
    post_id = len(my_posts)
    new_post = post.model_dump()
    new_post['id'] = post_id
    my_posts[post_id] = new_post
    return {"post created!" : new_post}


@app.get("/posts")
def get_posts():
    return {"data" : [x for x in my_posts.values()]}


@app.get("/posts/latest")
def get_latest():
    return {"data": my_posts[len(my_posts) - 1]}


@app.get("/posts/{post_id}")
def get_post(post_id: int, response: Response):
    post = None
    try:
        post = my_posts[post_id]
    except KeyError:
        response.status_code = status.HTTP_404_NOT_FOUND
    return { "data": post }
