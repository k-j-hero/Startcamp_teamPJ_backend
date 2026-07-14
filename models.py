from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Post(Base):
    __tablename__ = "posts" # 데이터베이스에서 사용할 테이블 이름

    id = Column(Integer, primary_key=True, index=True) # 글 번호 (자동 증가)
    category = Column(String, index=True) # 카테고리 (관광, 맛집 등)
    title = Column(String, nullable=False) # 제목 (필수 입력)
    content = Column(Text, nullable=False) # 본문 (필수 입력)
    password = Column(String, nullable=False) # 수정/삭제용 비밀번호 (필수 입력)
    view_count = Column(Integer, default=0) # 조회수 (기본값 0)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) # 작성 시간
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) # 수정 시간