from media import Media

class Series(Media):
    def __init__(self,name,director,IMDB,duration,Url,name_a1,age1,name_a2,age2,season,episode):
        super().__init__(name,director,IMDB,duration,Url,name_a1,age1,name_a2,age2)
        self.s = season
        self.e = episode