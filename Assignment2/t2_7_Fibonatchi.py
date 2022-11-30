
print("this programm is for making the Fibonacci sequence")
n=int(input("please enter n:"))
a=0
b=1
if n==0:
    print("Invalid number")
if n>=1:
    print(a)
if n>=2:
    print(b)
if n>2:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

