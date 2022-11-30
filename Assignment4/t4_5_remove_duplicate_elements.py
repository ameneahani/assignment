# Remove duplicate elements
list=[]
num=0
print("enter number or type end to end the list")

while num != "end":
    num=input("number or end:")
    if num != "end":
        list.append(int(num))
print(list)

for i in range (len(list)-1):
    n=i+1
    while n < len(list):
        if list[i] == list[n]:
            list.pop(n)
            n -= 1
        n += 1

print(list)