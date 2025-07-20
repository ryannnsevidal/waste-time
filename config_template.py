# copy this to config.py and put your real api keys

# openai key for gpt and whisper stuff
# get from https://platform.openai.com/api-keys
OPENAI_API_KEY = "your_openai_api_key_here"

# elevenlabs key for voice generation
# get from https://elevenlabs.io/
ELEVEN_LABS_KEY = "your_elevenlabs_api_key_here"

# slack webhook if you want notifications
# create at https://api.slack.com/messaging/webhooks
SLACK_WEBHOOK_URL = "your_slack_webhook_url_here"

# twilio stuff for phone calls
# get from https://console.twilio.com/
TWILIO_AUTH = {
    "account_sid": "your_twilio_account_sid_here",
    "auth_token": "your_twilio_auth_token_here", 
    "phone_number": "your_twilio_phone_number_here"
}
