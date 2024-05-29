from pydantic import BaseModel
from typing import Optional

#Entidad users
class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
