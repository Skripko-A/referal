from sqlalchemy.orm import Session
from db.repository.user import create_new_user
from schemas.user import UserCreate


def create_random_user(db: Session):
    user_data = UserCreate(email="random@user.com", password="password")  # Создаем данные пользователя
    new_user = create_new_user(user=user_data, db=db)  # Создаем нового пользователя в базе данных
    return new_user
