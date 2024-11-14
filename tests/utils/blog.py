from sqlalchemy.orm import Session
from db.repository.blog import create_new_blog
from schemas.blog import CreateBlog
from tests.utils.user import create_random_user


def create_random_blog(db: Session):
    # Создаем экземпляр CreateBlog
    blog_data = CreateBlog(title="random_title", content="this is a test random blog")
    
    # Создаем случайного пользователя
    new_random_user = create_random_user(db=db)
    
    # Создаем новый блог в базе данных
    new_random_blog = create_new_blog(
        blog=blog_data,  # Передаем данные блога
        db=db,
        author_id=new_random_user.id  # Передаем ID случайного пользователя как автора
    )
    return new_random_blog