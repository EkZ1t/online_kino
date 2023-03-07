
from app.models.base_model import AbstractModel
import peewee as pw


class Genre(AbstractModel):
    title = pw.CharField(100, unique=True)

class Post(AbstractModel):
    title = pw.CharField(100)
    description = pw.TextField(null=True)
    year = pw.DateField(formats=['%Y'])
    country = pw.CharField(20)
    genre = pw.ManyToManyField(Genre, backref='films')

PostGenres = Post.genre.through_model