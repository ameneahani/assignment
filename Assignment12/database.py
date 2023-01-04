from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

class Database():
    def read(self,MEDIA):
        f = open("assignment\Assignment12\youtube_url.txt","r")
        for line in f:
            result = line.split(",")
            if result[0] == "film":
                media = Film(result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9].replace("\n",""))
            elif result[0] == "series":
                media = Series(result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9],result[10],result[11].replace("\n",""))
            elif result[0] == "documentary":
                media = Documentary(result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9].replace("\n",""))
            elif result[0] == "clip":
                media = Clip(result[1],result[2],result[3],result[4],result[5],result[6],result[7],result[8],result[9].replace("\n",""))
            MEDIA.append(media)
        f.close()
        return MEDIA   

    def write(self,MEDIA):
        f = open("assignment\Assignment12\youtube_url.txt","w")
        for media in MEDIA:
            if type(media) == Film:
                f.write('film'+ ',')
            elif type(media) == Series:
                f.write('series'+ ',')
            elif type(media) == Documentary:
                f.write('documentary'+ ',')
            elif type(media) == Clip:
                f.write('clip'+ ',')
            f.write(media.name+ ',')
            f.write(media.dir+ ',')
            f.write(media.imdb+ ',')
            f.write(media.du+ ',')
            f.write(media.url+ ',')
            f.write(media.cast1.name+ ',')
            f.write(media.cast1.age+ ',')
            f.write(media.cast2.name+ ',')
            f.write(media.cast2.age)
            if type(media) == Series:
                f.write(','+ media.s+ ',')
                f.write(media.e )
            f.write('\n')
        f.close()
# db = Database()
# MEDIA =[]
# db.read(MEDIA)
# print(MEDIA)