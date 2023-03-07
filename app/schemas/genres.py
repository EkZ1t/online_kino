#TODO: написать схемы для жанров

from pydantic import BaseModel

class ShowGenre:
    title: str 
    
    class config:
        orm_mode = True 
        
class CreateGenre:
    title: str 
    
    class config:
        orm_mode = True