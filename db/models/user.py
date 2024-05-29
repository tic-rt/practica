from pydantic import BaseModel

#Entidad users
class User(BaseModel):
    id: int | None
    username: str
    email: str
