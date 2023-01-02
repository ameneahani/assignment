from media import Media
from database import Database

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Download")
    print("7- Exit")

#...........................................
MEDIA = []
print("Welcome to Filmstore")
print("loadting ...")
print("Data loaded")
data_base = Database()
MEDIA = data_base.read(MEDIA)

while True:
    show_menu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        Media.add(MEDIA)
    
    if choice == 2:
        user_input = input("Enter name of film that you want to edit :")
        for media in MEDIA:
            if media.name == user_input:
                media.edit()
                break
        else:
            print("Not found")

    if choice == 3:
        user_input = input("Enter name of the film that you want to remove :")
        for media in MEDIA:
            if media.name == user_input:
                media.remove(MEDIA)
                break
        else:
            print("Not found")

    if choice == 4:
        user_input = input("Enter information of media :")
        for media in MEDIA:
            m = [media.name,media.dir,media.du,media.imdb,media.casts]
            if user_input in m:
                media.search(MEDIA)
                break
        else:
            print("Not found")


    if choice == 5:
        print("name\t\t\t\tdirector\t\t\tIMDB\t\tduration\t\tcasts")
        for media in MEDIA:
            print(media.name,'\t',media.dir,'\t',media.imdb,'\t\t',media.du,'\t\t\t',media.casts)

    if choice == 6:
        user_input = input('Enter name of media :')
        for media in MEDIA:
            if media.name == user_input:
                media.download()
        else:
            print('Not found')

    if choice == 7:
        data_base.write(MEDIA)
        exit(0)

