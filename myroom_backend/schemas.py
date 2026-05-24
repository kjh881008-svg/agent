from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# --- User Schemas ---
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password_hash: str # 비밀번호 해시를 받음

class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True # SQLAlchemy 모델을 받아서 검증할 수 있게 함

# --- Content Schemas ---
class ContentBase(BaseModel):
    title: str
    body: str
    author_id: int

class ContentCreate(ContentBase):
    pass # ContentBase를 그대로 사용

class ContentRead(ContentBase):
    id: int
    published_at: datetime
    
    class Config:
        orm_mode = True

# --- Payment Schemas ---
class PaymentCreate(BaseModel):
    user_id: int
    amount: float
    payment_method: str
    transaction_id: str # 외부 PG사에서 받은 고유 트랜잭션 ID

class PaymentRead(BaseModel):
    id: int
    user_id: int
    amount: float
    payment_method: str
    transaction_id: str
    is_success: bool
    paid_at: datetime
    
    class Config:
        orm_mode = True