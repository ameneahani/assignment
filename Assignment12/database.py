from media import Media
class Database():

    def read(self,MEDIA):
        
        f = open("assignment\database_film",'r')
        for line in f:
            result = line.split(",")
            media = Media(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
            MEDIA.append(media)
        f.close()
        return MEDIA   

    def write(self,MEDIA):
        f = open("assinment\database_film","w")
        for media in MEDIA:
            f.write(media.name+ ',')
            f.write(media.dir+ ',')
            f.write(media.imdb+ ',')
            f.write(media.du+ ',')
            f.write(media.url+ ',')
            f.write(media.casts)
        f.close()
