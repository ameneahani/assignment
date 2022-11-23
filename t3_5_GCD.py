# GCD
first_num=int(input("enter your first number:"))
second_num=int(input("enter your second number:"))

if first_num>second_num:
    small_num=second_num
else:
    small_num=first_num
for i in range(1,small_num+1):
    if first_num % i ==0 and second_num % i ==0:
        GCD=i
print("GCD =",GCD)


