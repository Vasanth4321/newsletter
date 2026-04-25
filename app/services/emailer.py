import os
import requests

class EmailSender:
    def __init__(self):
        self.api_key = os.getenv("MAILGUN_API_KEY")
        self.domain = os.getenv("MAILGUN_DOMAIN")
        self.from_email = os.getenv("FROM_EMAIL", f"briefing@{self.domain}")
        self.to_email = os.getenv("RECIPIENT_EMAIL")

        if not all([self.api_key, self.domain, self.to_email]):
            raise ValueError("MAILGUN_API_KEY, MAILGUN_DOMAIN, and RECIPIENT_EMAIL environment variables required")

    def send_newsletter(self, html_content: str):
        url = f"https://api.mailgun.net/v3/{self.domain}/messages"

        data = {
            "from": f"Daily AI/Data Briefing <{self.from_email}>",
            "to": self.to_email,
            "subject": "📬 Daily AI/Data Briefing",
            "html": html_content
        }

        try:
            response = requests.post(
                url,
                auth=("api", self.api_key),
                data=data
            )
            response.raise_for_status()
            print(f"Email sent successfully! Status: {response.status_code}")
        except Exception as e:
            print(f"Error sending email: {e}")