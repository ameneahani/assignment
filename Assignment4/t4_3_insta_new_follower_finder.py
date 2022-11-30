import instaloader
import getpass

f = open("followers.txt","r")
old_followers=[]
for line in f:
    old_followers.append(line)
f.close()

L=instaloader.Instaloader()
user=input("username:")
password=getpass.getpass("password:")
L.login(user,password)
print("log in successfully!")
profile=instaloader.Profile.from_username(L.context,"amene ahani")

new_followers=[]
for follower in profile.get_followers:
    new_followers.append(follower)

for new_foll in new_followers:
    if new_foll not in old_followers:
        print(new_foll)

f=open("followers.txt","w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()