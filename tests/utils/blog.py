from sqlalchemy.orm import Session
from db.repository.blog import create_new_blog
from schemas.blog import CreateBlog
from tests.utils.user import create_random_user


def create_random_blog(db: Session):
    blog_data = CreateBlog(title="random_title", content="this is a test random blog")

    new_random_user = create_random_user(db=db)

    new_random_blog = create_new_blog(
        blog=blog_data,
        db=db,
        author_id=new_random_user.id,
    )
    return new_random_blog
