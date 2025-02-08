import requests
import json


# Usando a API do ChatGPT para responder uma pergunta

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer xxxxxxxxxxxxxxxxx" # Apenas para teste... key invalida
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]

}

resposta = requests.post(url, headers=headers, data=json.dumps(data))

print(resposta.json())
