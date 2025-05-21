class positions:
    def __init__(self,x=0,y=0,location=0):
        self.y=y
        self.x=x
        self.location=location



    def set_location(self,location):
        assert location >=0,("negative", location)
        self.location=location

    def map(self):
        if self.location<4:
            return "farm"
        elif self.location>4:
            return"bunker"
        else:
            return "silo"
    

while True:
    c1=int(input("number="))

    l1=positions()

    l1.set_location(c1)

    print(l1.map())
        