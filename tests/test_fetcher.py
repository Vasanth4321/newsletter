import pytest
from app.services.fetcher import ArticleFetcher

def test_fetch_articles():
    fetcher = ArticleFetcher()
    articles = fetcher.fetch_articles()
    assert len(articles) > 0
    assert all(hasattr(a, 'title') for a in articles)