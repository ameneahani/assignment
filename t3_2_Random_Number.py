# Generating a random array without duplicate elements
import random
n =int(input("enter n:"))
random_number=[]
while len(random_number)<n:
    rand=random.randint(0,3*n)
    if rand not in random_number :
        random_number.append(rand)
print(random_number)
