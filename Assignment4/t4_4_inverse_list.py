# make inverse of a list
list=[]
inverse_list=[]
num=print("enter a number or type end to end the list")
while num != "end" :
    num=input("number or end:")
    if num!="end":       
        list.append(int(num))
print (list)
for i in  range (1,len(list)+1):
    inverse_list.append(list[len(list)-i])

print (inverse_list)

