
class Media:
    def __init__(self,name,director,IMDB,duration,Url,name_a1,age1,name_a2,age2):
        self.name = name
        self.dir = director
        self.imdb = IMDB
        self.du = duration
        self.cast1 = Actor(name_a1,age1)
        self.cast2 = Actor(name_a2,age2)
        self.url = Url

    @staticmethod
    def add():
        name = input("Enter name :")
        dir = input("Enter director :")
        imdb = input("Enter IMDB :")
        du = input("Enter duration :")
        cast1_name = input("Enter name of first cast :")
        cast1_age = input("Enter age of first cast :")
        cast2_name = input("Enter name of second cast :")
        cast2_age = input("Enter age of second cast :")
        url = input("Enter Url :")
        return [name,dir,imdb,du,url,cast1_name,cast1_age,cast2_name,cast2_age]

    def edit(self):
        print("which field do you want to edit:")
        choi = int(input("1- name , 2- director , 3- IMBD , 4- duration , , 5- Url , 6- casts: "))
        if choi == 1:
            self.name = input("Enter new name:")
        elif choi == 2:
            self.dir = input("Enter new director:")
        elif choi == 3:
            self.imdb = input("Enter new IMDB:")
        elif choi == 4:
            self.du = input("Enter new duration:")
        elif choi == 5:
            self.url = input("Enter new Url:")
        elif choi == 6:
            self.cast1.name = input("Enter new name of cast1:") 
            self.cast1.age = input("Enter new age of cast1:")
            self.cast2.name = input("Enter newname of cast2:")
            self.cast2.age = input("Enter new age of cast2:")
        else:
            print("Invalid input")
        print("Information update successfully ")

    def remove(self,MEDIA):
        i = MEDIA.index(self)
        MEDIA.pop(i)

    def download(self):
        from pytube import YouTube
        yt = YouTube(self.url).streams.first().download()
        yt.streams.filter(progressive=True, file_extension='mp4')

class Actor:
    def __init__(self,name_a,age):
        self.name = name_a
        self.age = age


