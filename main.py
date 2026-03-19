import requests
import os

# GitHubの設定(Secrets)から読み込むように変更
api_key = os.environ.get("ANTHROPIC_API_KEY")

url = "https://api.anthropic.com/v1/messages"
headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

data = {
    "model": "claude-3-5-sonnet-20241022", # 最新のモデル名に修正
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, world"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
