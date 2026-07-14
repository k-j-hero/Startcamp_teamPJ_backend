from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 게시글 작성 요청 데이터 형식
class PostCreate(BaseModel):
    category: str
    title: str
    content: str
    password: str

# 게시글 조회 응답 데이터 형식
class PostResponse(PostCreate):
    id: int
    view_count: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True