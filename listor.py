index_clock=0
v=[]
Numbers=[33,41,33]

for Number in Numbers:
    index_clock+=1
    if index_clock==0:
        v=Number
    elif index_clock==1:
        if Number==v:
            Numbers.remove(index_clock)
        elif Number !=v:
            v2=Number
    if index_clock==2:
        if Number==v or Number==v2:
            Numbers.remove(index_clock)
        elif Number != v or Number!=v2:
            print


print(Numbers)
        

        
        




print(Number)

