from pydantic import BaseModel, EmailStr
from typing import Optional
#test commit
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
    
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class Customer(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None





