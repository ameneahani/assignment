#Rock_Paper_scissors
import random
print("welcome to Rock-Paper-Scissors Game")
print("this game is played in 5 rounds")
print("whenever you want to exit the game type exit")
computer_score=0
user_score=0
n=0

while True:
    n=n+1
    for i in range(5):
        x=random.randint(1,3)
        if x==1:
            computer_choice="rock"
        elif x==2:
            computer_choice="paper"
        elif x==3:
            computer_choice="scissors"

        user_choice=input("enter your choice: rock, paper, scissors:")
        if user_choice=="exit":
            break
        print("π»:",computer_choice)
        print("π§:",user_choice)
        if computer_choice=="rock" and user_choice=="paper":
            user_score=user_score+1
        elif computer_choice=="rock" and user_choice=="scissors":
            computer_score=computer_score+1
        elif computer_choice=="paper" and user_choice=="rock":
            computer_score=computer_score+1
        elif computer_choice=="paper" and user_choice=="scissors":
            user_score=user_score+1
        elif computer_choice=="scissors" and user_choice=="rock":
            user_score=user_score+1
        elif computer_choice=="scissors" and user_choice=="paper":
            computer_score=computer_score+1
        print("π§:",user_score,"π»:",computer_score)
    if user_choice=="exit":
        print("thanks, the end")
        break
    if computer_score>user_score:
        print("you lost π")
    elif computer_score<user_score:
        print("congrajulation,you winππ")
    else:
        print("you and computer are equal")
 
    print("do you want to play more?")   


