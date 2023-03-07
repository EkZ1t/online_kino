from app.queries.posts import get_all_films, create_post, get_film_by_id

from app.schemas.posts import PostCreateSchema
from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def get_films():
    return get_all_films()


@router.post('/create-post')
def create_film(film: PostCreateSchema):
    return create_post(film)

#TODO: дописать пути для остальных функций 