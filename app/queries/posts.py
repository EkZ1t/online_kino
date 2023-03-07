from datetime import date

from app.models.posts.post_model import Post, PostGenres, Genre
from app.models.base_model import db
from peewee import DoesNotExist, fn 
from typing import List 
from app.schemas.posts import PostOneSchema, PostAllSchema, PostCreateSchema 

# @db
# def create_post(title, desc, year: date, country, genres: List[str]) -> Post:
#     post = Post.create(
#         title=title,
#         description=desc,
#         year=year,
#         country=country
#     )
#     for genre in genres: 
#         g = Genre.get_or_create(title=genre)
#         post.genre.add(g)
#     return post

@db
def create_post(post_in: PostCreateSchema):
    post = Post.create(
        title = post_in.title,
        description = post_in.description,
        year = post_in.year,
        country = post_in.country 
    )
    for genre in post_in.genre:
        g = Genre.get(title=genre)
        post.genre.add(g)

@db
def get_all_films():
    posts = Post.select(Post.id ,Post.title, Post.year)
    return [PostAllSchema.from_orm(post) for post in posts]

@db
def get_film_by_id(id):
    post = Post.select(Post, fn.array_agg(Genre.title).alias('genre_titles')).join(PostGenres).join(Genre).where(Post.id == id).group_by(Post.id).get_or_none()
    return PostOneSchema.from_orm(post)
    # return {
    #     'id': post.id,
    #     'title': post.title,
    #     'year': post.year,
    #     'country': post.country,
    #     'genres': [genre.title for genre in post.genre]
    # }

@db 
def delete_post(title):
    post = Post.select().where(Post.title == title)
    return post



# TODO: дописать CRUD для моделей Posts
# TODO: ознакомиться с документацией 