import telegram
import myconfig

bot = telegram.Bot(token=myconfig.token)

def alert():
	with open ("states/active", "r") as myfile:
		data=myfile.read()
		if data!="1":
			picture = '1.jpg'
			video = '1.mp4'
			bot.sendPhoto(chat_id=myconfig.chat_id, photo=open(picture,'rb'))
			bot.sendDocument(chat_id=myconfig.chat_id, document=open(video,'rb'))
			text = 'Test'
			bot.send_message(myconfig.chat_id, text)

if __name__ == "__main__":
   alert()
