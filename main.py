from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/blog")
#we can give default values to the limit and bool
#we can pass any no.of parameters and assign them 
#optional
#for that import optioanl from typing
def user(limit = 10,published:bool=True,sort: Optional[str] = None):
    if published:
        return {"data":f"{limit} published blogs from db"}
    else:
        return {"data":f"{limit} blogs from db"}

     
@app.get("/blog/{blog_id}")
def data(blog_id:int):
    return {"data":blog_id}

@app.get('/blog/{id}/comments')
def comments(id):

    return {'data':[1,2,3]}


class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data':{f'blog is created with title as {request.title}'}}