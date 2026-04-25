from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Article(BaseModel):
    title: str
    link: str
    summary: Optional[str] = None
    published: Optional[datetime] = None
    category: Optional[str] = None

class Newsletter(BaseModel):
    date: datetime
    articles: List[Article]