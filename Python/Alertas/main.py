import requests
from pytgbot import Bot
from dados import API_KEY, CHAT

bot = Bot(API_KEY)

def enviar_telegram(cotacao):
    msg = f'Dolar menor que R$ 5.20, valor atual R$ {cotacao:.2f}'
    bot.send_message(CHAT, msg)
    

url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL'
response = requests.get(url)
response_dict = response.json()
cotacao = float(response_dict['USDBRL']['bid'])

enviar_telegram(cotacao)

