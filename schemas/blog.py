from typing import Optional
from datetime import datetime

from pydantic import BaseModel, model_validator, ConfigDict


class CreateBlog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        title = values.get('title')
        if title:
            values['slug'] = title.replace(" ", "-").lower()
        else:
            raise ValueError("Title is required to generate a slug")
        return values


class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
