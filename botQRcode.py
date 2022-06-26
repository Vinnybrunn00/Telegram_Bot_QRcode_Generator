import requests
import telebot
import qrcode
import time

token = 'Your_token'
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

						qr = qrcode.QRCode(
							version=1, 
							error_correction=qrcode.constants.ERROR_CORRECT_L,
							box_size=10,
							border=4
							)

						qr.add_data(input)
						qr.make(fit=True)

						img = qr.make_image(
							fill_color='black',
							back_color='white'
							)
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
						f'"{message.text}" - não encontrado'
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
