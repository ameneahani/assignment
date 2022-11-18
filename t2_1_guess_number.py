#Guess_number
import random
computer_number=random.randint(1,50)
print("welocome, lets play guess the number")
print("the number is between 1 and 50")
n=0
while True:
    for i in range(5):
        n=n+1
        user_number=int(input("enter your number"))
        if computer_number>user_number:
            print("go up")
        elif computer_number<user_number:
            print("go down")
        else: 
            print("congrajulation,you win after",n,"try")
            break
    if computer_number==user_number:
        break
    else:
        print("you try", n,"times")
        user_number=input("if you want to continue press a key or exit to end")
    if user_number=="exit":
        print("thanks, the end")
        break

        
