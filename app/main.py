from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

latest_post_id = -1
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
def create_pos(post: Post, response: Response):
    global latest_post_id
    post_id = len(my_posts)
    new_post = post.model_dump()
    new_post['id'] = post_id
    my_posts[post_id] = new_post
    latest_post_id = post_id
    response.status_code = status.HTTP_201_CREATED
    return {"post created!" : new_post}


@app.get("/posts")
def get_posts():
    return {"data" : my_posts}


@app.get("/posts/latest")
def get_latest():
    if (latest_post_id == -1):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"nenhuma postagem encontrada!"
        )        
    return {"data": my_posts[latest_post_id]}


@app.get("/posts/{post_id}")
def get_post(post_id: int):
    post = None
    try:
        post = my_posts[post_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"post with id: {post_id} was not found"
        )
    return { "data": post }


@app.delete("/posts/{post_id}")
def delete_post(post_id: int, response: Response):
    if post_id in my_posts:
        del my_posts[post_id]
        response.status_code = status.HTTP_204_NO_CONTENT
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {post_id} does not exists"
        )
    return response


@app.put("/posts/{post_id}")
def put_post(post: Post, post_id: int):
    if (post_id not in my_posts):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"post with id {post_id} does not exists")
    new_post = post.model_dump()
    new_post['id'] = post_id
    my_posts[post_id] = new_post
    return {"new post": new_post}