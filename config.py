import telebot as tb
file = open('token.txt')
bot = tb.TeleBot(token=file.read())
file.close()
