class position:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=x

    
    def set_x(self,x):
        assert x >=0 , ("negative",x)
        self.x=x

    def set_y(self,y):
        assert y >=0 , ("negative",y)
        self.y=y



input(
    "Upp=1" \
    "Down=0" \
    "Left=2" \
    "Right=3"
)
    
