from config import bot
from random import randint
from time import sleep


G_PARK_WORDS = [ #Theese words tested every time plain text is sent.
    "расскажи",
    "покажи",
    "дай",
    "подскажи",
    "скажи",
    "найди",
    "вспомни",
    "передай",
    "парк"
]

#----------------------------------------------#
# start_bot( message )
# Called when bot starts
@bot.message_handler(commands='start')
def start_bot(msg):
    file = open('greet_phrases.txt', encoding='utf-8')
    phrases = file.read().split('\n')
    file.close()
    rnd_phrase = phrases[randint(0, len(phrases) - 1)]
    split_and_out(msg.chat.id, rnd_phrase)

#----------------------------------------------#
# split_and_out( id, message )
# Handy method to send messages
def split_and_out(id, text):
    split_strings = []
    for index in range(0, len(text), 1000):
        split_strings.append(text[index: index + 1000])
    for el in split_strings:
        bot.send_message(id, el)
        sleep(1)


#----------------------------------------------#
# fairytale( message )
# Sends user a fairy tale
@bot.message_handler(commands='сказка')
def fairytale(msg):
    file = open('tales.txt', 'r', encoding='utf-8')
    text = file.read().split('$')
    file.close()
    choice = randint(0, len(text) - 1)
    split_and_out(msg.chat.id, text[choice])

#----------------------------------------------#
# travelTip( message )
# Sends user a travel tip
@bot.message_handler(commands='совет')
def travelTip(msg):
    file = open('tips.txt', 'r', encoding='utf-8')
    text = file.read().split('\n')
    file.close()
    choice = randint(0, len(text) - 1)
    split_and_out(msg.chat.id, text[choice])

#----------------------------------------------#
# genericPhrase( )
# Sends user a generic phrase
def genericPhrase():
    file = open('random_phrases.txt', 'r', encoding='utf-8')
    text = file.read().split('\n')
    file.close()
    choice = randint(0, len(text) - 1)
    return text[choice]


#----------------------------------------------#
# command_hanadler( message )
# Hook for plain text
@bot.message_handler(content_types=['text'])
def command_hanadler(msg):
    x = plane_text_handler(msg.text)
    split_and_out(msg.chat.id, x)

#----------------------------------------------#
# command_hanadler( message )
# Called to generate park ad phrase
def stock_phrase(name, link):
    file = open('park_phrases.txt', encoding='utf-8')
    phrases = file.read().split('\n')
    file.close()
    rnd_phrase = phrases[randint(0, len(phrases) - 1)].replace('{parkname}', name)
    return rnd_phrase + '\n' + link

#----------------------------------------------#
# plane_text_handler( message )
# Called when there's nothing to answer
def plane_text_handler(text):
    global G_PARK_WORDS

    file = open('parks.txt', 'r', encoding='utf-8')
    data = file.read().split('\n') #All known parks stored in file
    file.close()
    parks = []

    for element in data: #We're going to split 'em
        parks.append(element.split(' ', 1))

    for pair in parks:  #Search for possible parks if avaible
        if pair[1].lower() in text.lower():
            return stock_phrase(pair[1], pair[0])

    #If there's no parks found we should check if user exactly wants to get park
    noWords = True
    if not "парк" in text.lower():
        return genericPhrase()

    for test_word in G_PARK_WORDS:
        if test_word in text.lower():
            noWords = False
            break
    if noWords:
        return genericPhrase()

    rand_park = parks[ randint(0, len(parks) - 1) ]
    return stock_phrase(rand_park[1], rand_park[0])