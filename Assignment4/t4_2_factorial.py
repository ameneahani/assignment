#  factorial number Detector
num=int(input("enter the number:"))
factorial=[]
x=1
i=0

while x <= num:
    i += 1
    x=x*i
    factorial.append(x)
if num in factorial:
    print("yes")
else:
    print("No")
