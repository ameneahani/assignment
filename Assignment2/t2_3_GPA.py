#GPA calculator
print("hi, welcome to GPA calculator")
print("whenever you want to exit type exit")
sum=0
n=0
while True:
    n=n+1 
    a=input("please enter your number:")
    if a=="exit":
        print("thanks, the end")
        break
    score=float(a)
    sum=score+sum
    print(sum)
    print(n)
average=sum/n
print("your average is:",average)


