from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.base_model import db_connection, db 
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id, delete_post
from app.schemas.posts import PostCreateSchema
from datetime import date 
from app.routes.posts import router 

from fastapi import FastAPI


@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])


app = FastAPI()
app.include_router(router)
