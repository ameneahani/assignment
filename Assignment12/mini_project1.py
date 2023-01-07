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

def show_info(media):
    if type(media) == Series:
            type_media = 'series'
            data = [media.name,media.dir,media.imdb,media.du,media.cast1.name+','+media.cast2.name,type_media,media.s+','+media.e.replace('\n','')]
    else:
        if type(media) == Film:
            type_media = 'film'
        elif type(media) == Documentary:
            type_media = 'documentary'
        elif type(media) == Clip:
            type_media = 'clip'
        data = [media.name,media.dir,media.imdb,media.du,media.cast1.name+','+media.cast2.name,type_media]
    draw_table(data)

#........................ # draw_table
def draw_header():
    header = ['Name','Director','IMDB','Duration','Casts','Type','Se'+ '/'+'Ep']
    print("*"*132)
    l = [20,23,8,9,40,12,8]
    i = 0
    for column in header:
        print("#",end = " ")
        print(fixed_length(column,l[i]),end ="")
        i += 1
    print()
    print("*"*132)
    
def draw_table(data):
    l = [20,23,8,9,40,12,8]
    i = 0
    for column in data:
        print("#",end = " ")
        print(fixed_length(column,l[i]),end ="")
        i += 1
    print()

def draw_down():
    print("*"*132)

def fixed_length(text,length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " *length)[:length]
        return text
#........................................ main
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
        if choi in [1,2,3,4]:
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
        else:
            print("Invalid input")
            
    elif choice == 2:
        user_input = input("Enter name of film that you want to edit :")
        for media in MEDIA:
            if media.name.lower() == user_input.lower():
                print(media.name)
                media.edit()
                break
        else:
            print("Not found!")

    elif choice == 3:
        user_input = input("Enter name of the film that you want to remove :")
        for media in MEDIA:
            if media.name.lower() == user_input.lower():
                media.remove(MEDIA)
                break
        else:
            print("Not found!")

    elif choice == 4:
        print("1- Information of media, 2- Duration between time a and b (min) ")
        choi = int(input("Enter your choice :"))
        if choi == 1:
            user_input = input("Enter some information of media:(name/director/duration/imdb/casts)")
            for media in MEDIA:
                m = [media.name.lower(),media.dir.lower(),media.du,media.imdb,media.cast1.name.lower(),media.cast2.name.lower()]
                if user_input.lower() in m:
                    draw_header()
                    show_info(media)
                    draw_down()
                    break
            else:
                print("Not found")
        elif choi == 2:
            a = int(input("Enter time a:"))
            b = int(input("Enter time b:" ))
            draw_header()
            for media in MEDIA:
                if a <= int(media.du) <= b:
                    show_info(media)
            draw_down()
        else:
            print("Invalid input!")

    elif choice == 5:
        draw_header()
        for media in MEDIA:
            show_info(media)
        draw_down()

    elif choice == 6:
        user_input = input('Enter name of media :')
        for media in MEDIA:
            if media.name.lower() == user_input.lower():
                media.download()
        else:
            print('Not found')

    elif choice == 7:
        data_base.write(MEDIA)
        exit(0)
    else:
        print("Invalid inpur! Try again")

