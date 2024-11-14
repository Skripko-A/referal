from typing import Optional
from datetime import datetime

from pydantic import BaseModel, model_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        title = values.get('title')
        if title:
            slug = title.replace(" ", "-").lower()
        return slug


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config():
        from_attributes = True
