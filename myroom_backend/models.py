from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# 1. User Model (회원 정보)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False) # 실제로는 bcrypt 등으로 해시 처리 필수
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

# 2. Content Model (콘텐츠 정보)
class Content(Base):
    __tablename__ = "contents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    body = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id")) # FK 연결
    published_at = Column(DateTime, default=datetime.utcnow)
    # 관계 설정: 한 명의 사용자는 여러 개의 콘텐츠를 가질 수 있다.
    author = relationship("User", back_populates="contents")

# 3. Payment Model (결제 정보)
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False) # 카드, 간편결제 등
    transaction_id = Column(String, unique=True, nullable=False)
    is_success = Column(Boolean, default=False)
    paid_at = Column(DateTime, default=datetime.utcnow)
    
    # 관계 설정
    user = relationship("User", back_populates="payments")