import os
from datetime import datetime
from tavily import TavilyClient
from app.models.article import Article

class ArticleFetcher:
    """Fetch latest AI/ML/Data Science articles using Tavily search API"""
    
    def __init__(self):
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY environment variable not set")
        self.client = TavilyClient(api_key=api_key)
    
    SEARCH_QUERIES = [
        "machine learning breakthrough 2026",
        "artificial intelligence latest news",
        "data science tools and techniques",
        "AI research papers",
        "deep learning new methods",
        "large language models updates",
        "data engineering infrastructure",
        "AI ethics and governance"
    ]

    def fetch_articles(self) -> list[Article]:
        """Fetch articles from Tavily across multiple search queries"""
        articles = []
        
        for query in self.SEARCH_QUERIES:
            try:
                response = self.client.search(query, max_results=5)
                
                for result in response.get("results", []):
                    article = Article(
                        title=result.get("title", ""),
                        link=result.get("url", ""),
                        summary=result.get("content", "")[:500],
                        published=datetime.now(),
                        category=None
                    )
                    articles.append(article)
            except Exception as e:
                print(f"Error searching '{query}': {e}")
        
        return articles