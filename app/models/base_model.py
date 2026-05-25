from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy의 기본 베이스 클래스 정의
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())

class Content(Base):
    __tablename__ = "contents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author_id = Column(Integer, index=True) # Foreign Key: User.id
    body = Column(String, nullable=False)
    is_published = Column(Integer, default=0) # 0: 비공개, 1: 공개
    created_at = Column(DateTime, default=func.now())

# 결제 모듈은 추후 Payment 테이블과 별도의 서비스 계층으로 분리하는 것이 좋으나,
# 일단 스키마 정의를 위해 Placeholder만 남깁니다.
# class Payment(Base):
#     __tablename__ = "payments"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer)
#     amount = Column(Integer)
#     status = Column(String)