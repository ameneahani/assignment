# Translate app

import gtts
import os

def read_from_database():
    global WORDS
    WORDS = []
    words=[]
    file_list=os.listdir("Assignment8")
    # print(file_list)
    if "translate1.txt" in file_list:
        f = open("Assignment8/translate1.txt",'r')
        words=f.read().split("\n")
        f.close()
        for i in range (0,len(words),2):
            word_dict = {'eng':words[i],'fa':words[i+1]}
            WORDS.append(word_dict)
    else:
        print("Database not found")
        exit(0)


def write_to_database():
    f = open("Assignment8/translate1.txt",'w')
    for word in WORDS:
        f.write(word['eng']+'\n')
        f.write(word['fa']+'\n')
    f.close()


def show_menu():
    print("1- Translate Persian to English")
    print("2- translate English to Persian")
    print("3- Add a word to the word bank")
    print("4- Exit")

def translate_per_to_eng():
    user_sentence=[]
    output = ""
    user_text = input("plese enter your text and put (.) between two sentences : ")
    user_sentences = user_text.split(".")
    for user_sen in user_sentences:
        user_sentence.append(user_sen.split(" "))
    for user_words in user_sentence:
        for user_word in user_words:
            for word in WORDS:
                if user_word == (word['fa']):
                    output =  output + word['eng'] + " "
                    break
            else:
                output =  output + user_word + " "
        output = output + "."
    print(output)
    return(output)


def translate_eng_to_per():
    user_sentence=[]
    output = ""
    user_text = input("plese enter your text and put (.) between two sentences : ")
    user_sentences = user_text.split(".")
    for user_sen in user_sentences:
        user_sentence.append(user_sen.split(" "))
    for user_words in user_sentence:
        for user_word in user_words:
            for word in WORDS:
                if user_word == (word['eng']):
                    output =  output + word['fa'] + " "
                    break
            else:
                output =  output + user_word + " "
        output = output + "."
    print(output)
    return(output)

def add():
    eng_word=input("please anter your english word :")
    fa_word = input("please enter its translate in persian :")
    my_dict = {'eng':eng_word,'fa':fa_word}
    WORDS.append(my_dict)


def convert_text_to_audio(lan,text):
    audio = gtts.gTTS(text, lang=lan,slow=False)
    audio.save("Assignment8/audio.mp3")





print(" Welcome to translation application")
read_from_database()
while True:
    show_menu()
    user_choice = int(input("enter your choice: "))
    if user_choice == 1:
        text = translate_per_to_eng()
        lan = "en"
        convert_text_to_audio(lan,text)
    elif user_choice == 2:
        text = translate_eng_to_per()
        lan = "ar"
        convert_text_to_audio(lan,text)
    elif user_choice == 3:
        add()
    elif user_choice == 4:
        write_to_database()
        exit(0)

    



