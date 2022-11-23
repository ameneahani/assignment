# Detect if an array is sort or not
s=[]
a=0
not_sort=0
sort=0
while a != "end":
    a = input("enter your value or  type end:")
    if a!= "end":
        s.append(int(a))
        
print(s)
for i in range(len(s)-1):
    if s[i]>s[i+1]:
        print("this array isnt sort")
        not_sort +=1
        break
if not_sort==0:
    print("this array is sort")



