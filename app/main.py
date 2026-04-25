from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.newsletter import router as newsletter_router

app = FastAPI(title="Data Science Newsletter", description="Daily newsletter for Data Science articles")

templates = Jinja2Templates(directory="app/templates")

app.include_router(newsletter_router)

@app.get("/", response_class=HTMLResponse)
async def dashboard(request):
    # Placeholder for dashboard
    return templates.TemplateResponse("dashboard.html", {"request": request, "newsletters": []})