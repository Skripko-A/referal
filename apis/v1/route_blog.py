from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from db.repository.blog import create_new_blog, retrieve_blog, get_active_blogs

router = APIRouter()


@router.post(
        "/blogs",
        response_model=ShowBlog,
        status_code=status.HTTP_201_CREATED
        )
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail="Блог не найден",
            status_code=status.HTTP_404_NOT_FOUND
            )


@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    all_blogs = get_active_blogs(db=db)
    return all_blogs


@router.put("/blog/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, author_id=1, db=db)
    if not blog:
        raise HTTPException(detail="Блог не найден")
    return blog
