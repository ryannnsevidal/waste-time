import requests
from config import SLACK_WEBHOOK_URL

def send_report(message):
    requests.post(SLACK_WEBHOOK_URL, json={"text": message})
