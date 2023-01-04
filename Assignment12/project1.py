from media import Media
from database import Database
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Download")
    print("7- Exit")

def draw_table(data,header):
    print("*"*135)
    lenth = [20,23,8,14,40,8,8]
    i = 0
    for column in header:
        print("#",end = " ")
        print(fixed_length(column,lenth[i]),end ="")
        i += 1
    print()
    print("*"*135)
    
    for row in data:
        i = 0
        for column in row :
            print("#",end = " ")
            print(fixed_length(column,lenth[i]),end ="")
            i += 1
        print()
    print("*"*135)

def fixed_length(text,length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " *length)[:length]
        return text
#...........................................
MEDIA = []
print("Welcome to mediastore")
print("loadting ...")
print("Data loaded")
data_base = Database()
MEDIA = data_base.read(MEDIA)

while True:
    show_menu()
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("1- Film, 2- Series, 3- Documentary, 4- Clip")
        choi = int(input("Enetr type of media:"))
        m_add = Media.add()
        if choi == 1:
            media = Film(m_add[0],m_add[1],m_add[2],m_add[3],m_add[4],m_add[5],m_add[6],m_add[7],m_add[8])
        if choi == 2:
            media = Series(m_add[0],m_add[1],m_add[2],m_add[3],m_add[4],m_add[5],m_add[6],m_add[7],m_add[8],input("Enter season:"),input("Enter episod:"))
        if choi == 3:
            media = Documentary(m_add[0],m_add[1],m_add[2],m_add[3],m_add[4],m_add[5],m_add[6],m_add[7],m_add[8])
        if choi == 4:
            media = Clip(m_add[0],m_add[1],m_add[2],m_add[3],m_add[4],m_add[5],m_add[6],m_add[7],m_add[8])
        MEDIA.append(media)
        print("Information update successfully ")
    
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
            m = [media.name,media.dir,media.du,media.imdb,media.cast1.name,media.cast2.name]
            if user_input in m:
                media.search(MEDIA)
                break
        else:
            print("Not found")

    if choice == 5:
        DATA = []
        header = ['name','director','IMDB','duration(min)','casts','season','episode']
        for media in MEDIA:
            if type(media) == Series:
                data = [media.name,media.dir,media.imdb,media.du,media.cast1.name+','+media.cast2.name,media.s,media.e.replace('\n','')]
                print(data)
            else:
                data = [media.name,media.dir,media.imdb,media.du,media.cast1.name+','+media.cast2.name]
                print(data)
            print(data)
            DATA.append(data)
        draw_table(DATA,header)

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

