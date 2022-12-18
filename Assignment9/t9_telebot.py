import random
import qrcode
import telebot
import gtts
from telebot import types 
from datetime import date
import jdatetime


bot = telebot.TeleBot("5766145076:AAFOr79kAmq5vYgx70lb7HRwgB4r9aSEXsE",parse_mode=None)

@bot.message_handler(commands=['start'])
def send_wellcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message,"Wellcome dear " + user_name )
    markup = types.ReplyKeyboardMarkup()
    bts_names = ['/game','/age','/voice','/max','/argmax','/qrcode','/help']
    for button in bts_names:
        markup.add(types.KeyboardButton(button))
    message = bot.send_message(message.chat.id,"What do you want to do:\n/game\n/age\n/voice\n/max\n/argmax\n/qrcode\n/help",reply_markup=markup)


@bot.message_handler(commands=['game'])
def input_game(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.add('new game')
    message = bot.reply_to(message,"Guess a number between 1 to 50 :",reply_markup=markup)
    pc_num=random.randint(1,50)
    print(pc_num)
    bot.register_next_step_handler(message,game,pc_num)

def game(message,pc_num):
    user_choi = message.text
    print(user_choi)
    if user_choi == "new game" or user_choi == "/game":
        bot.send_message(message.chat.id,"New Game :")
        input_game(message)
    elif not user_choi.isdigit():
        message = bot.reply_to(message,"Invalid input, try again")
        bot.register_next_step_handler(message,game,pc_num)
    user_num = int(user_choi)
    if pc_num>user_num:
        bot.send_message(message.chat.id,"GO UP!")
        bot.register_next_step_handler(message,game,pc_num)
    elif pc_num<user_num:
        bot.send_message(message.chat.id,"GO DOWN!")
        bot.register_next_step_handler(message,game,pc_num)
    elif pc_num == user_num:
        bot.send_message(message.chat.id,"YOU WIN!")
        return



@bot.message_handler(commands=['age'])
def input_age(message):
    message = bot.send_message(message.chat.id,"enter your birthday : yy/mm/dd ")
    bot.register_next_step_handler(message,age)

def age(message):
    birthday = message.text
    print(birthday)
    birth = birthday.split("/")
    today_mi = date.today()
    today_sh = jdatetime.date.fromgregorian(day=today_mi.day,month=today_mi.month,year=today_mi.year)
    yy = today_sh.year
    mm = today_sh.month
    dd = today_sh.day
    y = yy - int(birth[0])
    m = mm - int(birth[1])
    d = dd - int(birth[2])
    if m <0:
        m = m + 12
        y = y - 1 
    if d <0:
        d = d + 30
    age = f"your age is :{y} years, {m} month, {d} day"
    bot.send_message(message.chat.id,age)
    

@bot.message_handler(commands=['voice'])
def input_voice(message):
    message = bot.send_message(message.chat.id,"enter your text in english :")
    bot.register_next_step_handler(message,voice)

def voice(message):
    txt = message.text
    print(txt)
    audio = gtts.gTTS(txt, lang="en",slow=False)
    audio.save("Assignment9/bot_audio.mp3")
    voice = open("Assignment9/bot_audio.mp3",'rb')
    bot.send_voice(message.chat.id,voice)


@bot.message_handler(commands=['max'])
def input_max(message):
    message = bot.send_message(message.chat.id,"enter your numbers:num1,num2,...")
    bot.register_next_step_handler(message,max)

def max(message):
    msg = message.text
    array = msg.split(",")
    print(array)
    max_num = 0
    for number in array:
        if max_num<float(number):
            max_num = float(number)
    print(max_num)
    txt = f"Max number is :{max_num}"
    bot.send_message(message.chat.id,txt)

    

@bot.message_handler(commands=['argmax'])
def input_argmax(message):
    message = bot.send_message(message.chat.id,"enter your numbers:num1,num2,...")
    bot.register_next_step_handler(message,argmax)

def argmax(message):
    msg = message.text
    array = msg.split(",")
    print(array)
    max_num = 0
    i=0
    for number in array:
        if max_num<float(number):
            max_num = float(number)
            index = i
        i += 1
    print(max_num)
    txt = f"index of the max number is :{index}"
    bot.send_message(message.chat.id,txt)

@bot.message_handler(commands=['qrcode'])
def input_qrcode(message):
    message = bot.send_message(message.chat.id,"enter your string that you want to conver to qrcode:")
    bot.register_next_step_handler(message,qr_code)

def qr_code(message):
    msg = message.text
    img = qrcode.make(msg)
    img.save("Assignment9/bot_qrcode.png")
    f = open("Assignment9/bot_qrcode.png",'rb')
    bot.send_photo(message.chat.id,f)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"""\
command /start
Print welcome with user name
command /game
Run the number guessing game. The user guesses a number and the bot guides (go up, go down, you win)
command /age
Get the date of birth in Hijri and calculate the age.
command /voice
Receive a sentence in English from the user and send it as voice.
command /max
Receive an array as 14,7,78,15,8,19,20 from the user and print the largest value.
command /argmax
Receive an array as 14,7,78,15,8,19,20 from the user and print the index of the largest value.
command /qrcode
Receive a string from the user and generate its qrcode.
    """)


bot.infinity_polling()

 









