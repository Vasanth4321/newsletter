# Data Science Daily Newsletter

A FastAPI application that generates and sends daily newsletters with articles from Data Science sources.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Download spaCy model: `python -m spacy download en_core_web_sm`
3. Set up SendGrid API key: `export SENDGRID_API_KEY=your_key`
4. Run the app: `uvicorn app.main:app --reload`

## Features

- Fetches articles from Towards Data Science and ODSC via RSS
- Categorizes articles into ML, AI, Big Data, etc.
- Generates HTML newsletter
- Sends via email
- Web UI for management

## Deployment

Deploy to Cloudflare using Wrangler for Workers (Python support).

For GitHub Actions, set SENDGRID_API_KEY in repository secrets.