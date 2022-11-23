# Hang Man Game
import random
print("Welcome to Hang Man's game:")

words=["book","bus","taxi","transport","tree","house","horse","bycicle","world","freedom","revolution","industry"]

true_char=[]
false_char=[]
user_mistake=0

x=random.randint(0,len(words)-1)
computer_word=words[x]

while user_mistake<6:
    dash=0
    for i in range(len(computer_word)):
      
        if computer_word[i] in true_char:
            print(computer_word[i],end=" ")
        else:
            print("- ",end="")
            dash += 1
    if dash == 0:
        print(" 👏👏 Well done, You Win")
        break

    user_char=input("enter your character:")
    if len(user_char)==1:
        user_char=user_char.lower()
        if user_char in computer_word:
            print("✔️")
            true_char.append(user_char)

        else:
            false_char.append(user_char)
            print("❌")
            user_mistake += 1
            if user_mistake==6:
                print("Game Over")
    else:
       print("invalid input")



    




