from app.models.article import Article

class ArticleCategorizer:
    def __init__(self):
        self.categories = {
            "Machine Learning": ["machine learning", "ml", "supervised learning", "unsupervised learning", "regression", "classification", "neural network", "deep learning", "svm", "random forest", "gradient boosting", "xgboost", "lightgbm", "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn", "model training", "feature engineering", "hyperparameter", "overfitting", "underfitting", "cross-validation", "ensemble methods"],
            "AI": ["artificial intelligence", "ai", "computer vision", "nlp", "natural language processing", "chatbot", "robotics", "reinforcement learning", "generative ai", "llm", "large language model", "gpt", "transformer", "bert"],
            "Big Data": ["big data", "hadoop", "spark", "data lake", "etl", "data warehouse", "kafka", "streaming", "apache", "distributed computing"],
            "Data Science": ["data science", "statistics", "eda", "exploratory data analysis", "data visualization", "matplotlib", "seaborn", "tableau", "power bi", "statistical modeling", "hypothesis testing", "a/b testing"]
        }

    def categorize_articles(self, articles: list[Article]) -> list[Article]:
        for article in articles:
            article.category = self._categorize(article.title + " " + (article.summary or ""))
        return articles

    def _categorize(self, text: str) -> str:
        text_lower = text.lower()
        for category, keywords in self.categories.items():
            if any(keyword in text_lower for keyword in keywords):
                return category
        return "General"