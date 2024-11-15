from sqlalchemy.orm import Session
from db.repository.user import create_new_user
from schemas.user import UserCreate


def create_random_user(db: Session):
    user_data = UserCreate(email="random@user.com", password="password")
    new_user = create_new_user(user=user_data, db=db)
    return new_user
