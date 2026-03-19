
import requests
import os

def run_agent():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    url = "https://api.anthropic.com/v1/messages"
    
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    # もっとも安価でエラーが出にくいモデル「Haiku」に設定しました
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": "Hello!"}]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

if __name__ == "__main__":
    run_agent()
