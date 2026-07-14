from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database, models, schemas
import data_loader

# 데이터베이스 테이블 생성
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# DB 세션 의존성 주입
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. 게시글 목록 조회
@app.get("/api/posts", response_model=list[schemas.PostResponse])
def read_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

# 2. 게시글 작성
@app.post("/api/posts", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# 3. 게시글 상세 조회 (조회수 증가 포함)
@app.get("/api/posts/{post_id}", response_model=schemas.PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    db_post.view_count += 1
    db.commit()
    return db_post

# 4. 게시글 수정 (비밀번호 확인)
@app.put("/api/posts/{post_id}")
def update_post(post_id: int, post_update: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    if db_post.password != post_update.password:
        raise HTTPException(status_code=403, detail="비밀번호가 일치하지 않습니다.")
    
    db_post.title = post_update.title
    db_post.content = post_update.content
    db.commit()
    return {"message": "수정 완료"}

# 5. 게시글 삭제 (비밀번호 확인)
@app.delete("/api/posts/{post_id}")
def delete_post(post_id: int, password: str, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    if db_post.password != password:
        raise HTTPException(status_code=403, detail="비밀번호가 일치하지 않습니다.")
    
    db.delete(db_post)
    db.commit()
    return {"message": "삭제 완료"}
# main.py

@app.get("/api/data/tourism")
def get_tourism():
    return data_loader.load_json_data("광주_전라권_관광지.json")

@app.get("/api/data/festivals")
def get_festivals():
    return data_loader.load_json_data("광주_전라권_축제공연행사.json")

@app.get("/api/data/leports")
def get_leports():
    return data_loader.load_json_data("광주_전라권_레포츠.json")

@app.get("/api/data/culture")
def get_culture():
    return data_loader.load_json_data("광주_전라권_문화시설.json")

@app.get("/api/data/shopping")
def get_shopping():
    return data_loader.load_json_data("광주_전라권_쇼핑.json")

@app.get("/api/data/stay")
def get_stay():
    return data_loader.load_json_data("광주_전라권_숙박.json")

@app.get("/api/data/courses")
def get_courses():
    return data_loader.load_json_data("광주_전라권_여행코스.json")

@app.get("/api/data/restaurants")
def get_restaurants():
    return data_loader.load_json_data("광주_전라권_음식점.json")