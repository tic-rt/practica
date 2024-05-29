from fastapi import APIRouter, HTTPException  
from pydantic import BaseModel


router = APIRouter(prefix="/user", tags=["Usuarios"], responses={404: {"message": "No encontrado"}})

#Entidad users

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "Mauro", surname = "Campani", url = "https://mauro.com", age = 35),
         User(id = 2,name = "Juan", surname = "asdasd", url ="https://juan.com", age = 38),
         User(id = 3,name = "pepe", surname = "asd", url ="https://pepe.com", age = 22)]



@router.get("/users")
async def users():
    return users_list


#Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)
    

#Query
@router.get("/")
async def user(id: int):
    return search_user(id)
    

@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="El usuario ya existe")
    
    users_list.append(user)
    return user


@router.put("/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@router.delete("/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuariod"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}