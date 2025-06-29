# from openai import OpenAI
# from  decouple import config

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key=config("API_KEY"),
# )

# completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   extra_body={},
#   model="deepseek/deepseek-chat-v3-0324:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "In less than 150 words, explain the meaning of life in simple, plain English. Avoid headings or formatting."
#     }
#   ]
# )
# print(completion.choices[0].message.content)