from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    id: Optional[UUID]
    firstName: str
    lastName: str
    middleName: Optional[str]
    gender: Gender
    roles: List[Role]


class UpdateUser(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    middleName: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]
