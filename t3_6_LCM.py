# LCM
first_num=int(input("enter your fisrt number:"))
second_num=int(input("enter your second number:"))
if first_num>second_num:
    max=first_num
    min=second_num
else:
    max=second_num
    min=first_num
for i in range(1,max+1):
    LCM=min*i
    if LCM % max ==0:
        break
print("LCM =",LCM)