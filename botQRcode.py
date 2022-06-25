import requests
import telebot
import qrcode
import time

token = '5389232508:AAFFBeHEkr41pQTpxfDI8OT5s16jSEdqDsk'
bot = telebot.TeleBot(token)

def QRCode(message):
	if message.text == message.text:
		input = message.text
		x = input.find('/')
		if x == -1:
			bot.reply_to(message, 
			f'"{message.text}" não é um link'
				)
		else:
			if len(input) > 8:
				try:
					site = requests.get(input)
					if site.status_code == 200:
						bot.reply_to(message, 'Aguarde...')
						img = qrcode.make(input)
						img.save('QRCODE.png')
						time.sleep(1.5)
						imagem = open('QRCODE.png', 'rb')
						bot.send_photo(message.chat.id, imagem)
					else:
						bot.send_message(message.chat.id, 
							f'"{message.text}" | Status code -> {site.status_code}'
								)
				except:
					bot.send_message(message.chat.id, 
						f'404 - "{message.text}" - não encontrado'
							)
			else:
				bot.send_message(message.chat.id, 
					'Use um link válido para gerar o QRCODE.'
				)
		return True
		
	else:
		return False

@bot.message_handler(func=QRCode)
def Start(message):
	pass

bot.infinity_polling()