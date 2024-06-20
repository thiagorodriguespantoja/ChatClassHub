# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from secrets_manager import get_secret

app = Flask(__name__)

# Obter a chave da API da função mockada
OPENAI_API_KEY = get_secret()

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()

    # Envie a mensagem para a API do ChatGPT (simulada)
    chatgpt_response = get_chatgpt_response(incoming_msg)
    msg.body(chatgpt_response)

    return str(resp)

def get_chatgpt_response(message):
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'text-davinci-003',
        'prompt': message,
        'max_tokens': 150
    }
    # Simular uma resposta para testes
    response = {
        "choices": [
            {"text": "This is a test response from ChatGPT"}
        ]
    }
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    app.run(debug=True)
