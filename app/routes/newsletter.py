from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.fetcher import ArticleFetcher
from app.services.categorizer import ArticleCategorizer
from app.services.emailer import EmailSender
from app.models.article import Newsletter
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/generate", response_class=HTMLResponse)
async def generate_newsletter(request: Request):
    fetcher = ArticleFetcher()
    categorizer = ArticleCategorizer()
    articles = fetcher.fetch_articles()
    categorized_articles = categorizer.categorize_articles(articles)
    
    # Group by category
    grouped = {}
    for article in categorized_articles:
        cat = article.category or "General"
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(article)
    
    newsletter = Newsletter(date=datetime.now(), articles=categorized_articles)
    
    return templates.TemplateResponse("newsletter.html", {
        "request": request,
        "newsletter": newsletter,
        "grouped_articles": grouped
    })

@router.post("/send")
async def send_newsletter():
    # Placeholder: In real app, get recipients from DB
    recipients = ["user@example.com"]  # Replace with actual subscribers
    
    fetcher = ArticleFetcher()
    categorizer = ArticleCategorizer()
    emailer = EmailSender()
    
    articles = fetcher.fetch_articles()
    categorized_articles = categorizer.categorize_articles(articles)
    
    # Generate HTML (simplified)
    html = "<h1>Daily Data Science Newsletter</h1>"
    for article in categorized_articles[:5]:  # Limit for demo
        html += f"<h2>{article.title}</h2><p>{article.summary}</p><a href='{article.link}'>Read more</a><br>"
    
    emailer.send_newsletter(html, recipients)
    return {"message": "Newsletter sent"}