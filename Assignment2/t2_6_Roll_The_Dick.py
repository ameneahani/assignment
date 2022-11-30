import random
print("Welcome")
while True:
    a=input("For rolling the Dick press a key:")
    dick=random.randint(1,6)
    print("🎲 :",dick)
    if dick==6:
        print("Great, you can roll it again")
    else:
        break
    

