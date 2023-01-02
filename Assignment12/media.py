
class Media:
    def __init__(self,name,director,IMDB,duration,year,country,Url,Actor):
        self.name = name
        self.dir = director
        self.imdb = IMDB
        self.du = duration
        self.year = year
        self.country = country
        self.casts = Actor()
        self.url = Url

    @staticmethod
    def add(MEDIA):
        name = input("Enter name :")
        dir = input("Enter director :")
        imdb = input("Enter IMDB :")
        du = input("Enter duration :")
        year = input("Enter year of film making :")
        country = input("Enter country :")
        casts = input("Enter casts :")
        url = input("Enter Url :")
        film = Media(name,dir,imdb,du,year,country,url,casts)
        MEDIA.append(film)

    def edit(self):
        print("which field do you want to edit:")
        choi = int(input("1- name , 2- director , 3- IMBD , 4- duration , 5- year , 6- country , 7- Url , 8- casts: "))
        if choi == 1:
            self.name = input("Enter new name:")
        elif choi == 2:
            self.dir = input("Enter new director:")
        elif choi == 3:
            self.imdb = input("Enter new IMDB:")
        elif choi == 4:
            self.du = input("Enter new duration:")
        elif choi == 5:
            self.year = input("Enter new year:")
        elif choi == 6:
            self.country = input("Enter new country:")
        elif choi == 7:
            self.url = input("Enter new Url:")
        elif choi == 8:
            self.casts = input("Enter new casts") 
        else:
            print("Invalid input")
        print("Information update successfully ")

    def remove(self,MEDIA):
        i = MEDIA.index(self)
        MEDIA.pop(i)

    def search(self,MEDIA):
        i = MEDIA.index(self)
        print("name\t\tdirector\t\tIMDB\t\tduration\t\tcasts")
        print(MEDIA[i].name,'\t',MEDIA[i].dir,'\t',MEDIA[i].imdb,'\t\t',MEDIA[i].du,'\t\t',MEDIA[i].casts)




    def showinfo(self):
        ...

    def download(self):
        from pytube import YouTube
        yt = YouTube(self.url).streams.first().download()
        yt.streams.filter(progressive=True, file_extension='mp4')


class Actor:
    def __init__(self,name,age):
        self.name = name
        self.age = age


