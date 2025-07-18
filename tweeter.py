from openai import OpenAI
from datetime import datetime, time
from decouple import config
import tweepy
import subprocess
subprocess.run(["python","extracter.py"])

now = datetime.now().time()
n=0
if now < time(6,00):
    n=1
elif now < time(12,00):
    n=2
elif now < time(18,00):
    n=3
elif now<time(23,59):
    n=4
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=config("API_KEY"),
)
tweet = None
with open(f"journal_{n}.txt","r") as f:
    prompt = f.read()
    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
        {
        "role": "user",
        "content": f"In less than 270 characters write this as tweet, {prompt}, plain English. Avoid headings or formatting. it should not seem like ai generation, dont use placeholders, donot mention chars count etc."
        }
    ]
    )
    matter = completion.choices[0].message.content
    print(matter)

api_key = config("X_API_KEY")
api_secret = config("X_API_SECRET")
access_token = config("X_ACCESS_TOKEN")
access_token_secret = config("X_ACCESS_SECRET")

# authentication
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

response = client.create_tweet(text=matter)
print("Tweeted")
    


