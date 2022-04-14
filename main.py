import telebot as tb
import traceback
from commands import *
from time import sleep
from config import bot

#----------------------------------------------#
# main_polling_loop( )
# Bot's main loop
def main_polling_loop():
    while True:
        try:
            bot.polling()
        except BaseException:
            traceback.format_exc()
            sleep(3)


if __name__ == '__main__':
    main_polling_loop()

