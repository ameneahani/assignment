from media import Media
class Series(Media):
    def __init__(self,part):
        super().__init__()
        self.part = part 