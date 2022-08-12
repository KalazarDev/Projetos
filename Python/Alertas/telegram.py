from pytgbot import Bot

API_KEY='5074322190:AAEK22WDSBGQbixbqyjaROEYlMVK0oHJPv8'  
CHAT='620079039'  

bot = Bot(API_KEY)

# sending messages:
msg = 'Teste'
bot.send_message(CHAT, msg)

# getting events:
for x in bot.get_updates():
	print(x)