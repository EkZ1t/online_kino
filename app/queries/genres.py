from app.models.posts.post_model import Genre
from app.models.base_model import db 
from peewee import IntegrityError, DoesNotExist

@db 
def create_genre(title):
    try:
        obj = Genre.create(title=title)
    except IntegrityError:
        obj = 0
    return obj

@db 
def delete_genre(title):
    try:
        obj = Genre.get(title=title)
        obj.delete_instance()
    except DoesNotExist: 
        return 0 
    return 1 

@db
def get_genres():
    return [genre.title for genre in Genre.select()]