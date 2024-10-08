from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


    class Config:
        orm_mode: True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: datetime
    owner: UserResponse


    class Config:
        orm_mode: True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int


    class Config:
        orm_mode: True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore
