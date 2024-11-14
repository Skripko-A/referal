from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def get_active_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs


def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    requested_blog = db.query(Blog).filter(Blog.id == id).first()
    if not requested_blog:
        return {"error": f"Blog with id {id} does not exist"}
    if not requested_blog.author_id == author_id:
        return {"error": "Вы не можете изменить"}
    requested_blog.title = blog.title
    requested_blog.content = blog.content
    db.add(requested_blog)
    db.commit()
    return requested_blog


def delete_blog(id: int, author_id: int, db: Session):
    requested_blog = db.query(Blog).filter(Blog.id == id)
    if not requested_blog.first():
        return {"error": f"Could not find blog with id {id}"}
    if not requested_blog.first().author_id == author_id:
        return {"error": "Only the author can delete a blog"}
    requested_blog.delete()
    db.commit()
    return {"УДалено": f"Блог номер {id}"}
