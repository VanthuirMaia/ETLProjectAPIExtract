import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


# Usando a API do ChatGPT para responder uma pergunta

url = "https://api.openai.com/v1/chat/completions"

openai_api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}


data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]

}

resposta = requests.post(url, headers=headers, data=json.dumps(data))

print(resposta.json())
