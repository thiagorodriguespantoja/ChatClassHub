from flask import Flask, request, jsonify
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Defina sua chave da API do OpenAI
OPENAI_API_KEY = 'sua-chave-api'

# Endpoint para receber mensagens do Twilio
@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()

    # Envie a mensagem para a API do ChatGPT
    chatgpt_response = get_chatgpt_response(incoming_msg)
    msg.body(chatgpt_response)

    return str(resp)

# Função para chamar a API do ChatGPT
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
    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()

if __name__ == '__main__':
    app.run(debug=True)
