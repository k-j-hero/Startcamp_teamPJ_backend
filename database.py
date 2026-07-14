from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite 데이터베이스 파일 경로 (현재 폴더에 localhub.db 파일이 생성됩니다)
SQLALCHEMY_DATABASE_URL = "sqlite:///./localhub.db"

# 데이터베이스와 통신할 엔진 생성
# check_same_thread=False는 SQLite가 여러 요청을 동시에 처리할 수 있게 해주는 설정입니다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터베이스와 대화할 세션(창구) 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델들이 상속받을 기본 클래스
Base = declarative_base()