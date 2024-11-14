from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from db.base_class import Base


class Blog(Base):
    __tablename__ = "blogs"  # Явно указываем имя таблицы
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=False)

    # Используйте правильное имя таблицы для ForeignKey
    author_id = Column(
        Integer, ForeignKey("users.id")
    )  # Исправлено на 'users'

    # Строковая ссылка на User
    author = relationship("User", back_populates="blogs")

    created_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=False)
