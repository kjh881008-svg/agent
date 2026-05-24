from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 환경 변수에서 DB URL을 가져와야 합니다. (예: postgresql://user:pass@host:port/dbname)
# 실제 환경에서는 .env 파일을 사용하고, os.environ.get('DATABASE_URL')을 사용해야 합니다.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" 

# 엔진 설정: SQLite를 임시로 사용합니다. 실제 운영 환경에서는 PostgreSQL/MySQL을 사용해야 합니다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 ORM 모델의 베이스 클래스
Base = declarative_base()

def get_db():
    """
    DB 세션을 제공하는 의존성(Dependency) 함수. 요청이 끝날 때 세션을 닫는 처리가 필수입니다.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()