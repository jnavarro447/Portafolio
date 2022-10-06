from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UpdateUser

app = FastAPI()

# Comando para correr el server
# uvicorn main:app --reload

db: List[User] = [
    User(
        id=UUID("84c0db9c-06db-43ee-82eb-8969ace79df0"),
        firstName="Jose",
        lastName="Navarro",
        middleName="Antonio",
        gender=Gender.male,
        roles=[Role.admin]
        ),
    User(
        id=UUID("6378ccc2-dd83-48f5-99a4-b58552a34d7f"),
        firstName="Camila",
        lastName="Santos",
        gender=Gender.female,
        roles=[Role.student]
        )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def insert_user(user: User):
    db.append(user)
    return {"id: ": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id{user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.firstName is not None:
                user.firstName = user_update.firstName
            if user_update.lastName is not None:
                user.lastName = user_update.lastName
            if user_update.middleName is not None:
                user.middleName = user_update.middleName
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
        raise HTTPException(
            status_code=404,
            detail=f"User with id{user_id} does not exists"
        )


