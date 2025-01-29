##2.2

area_eller_volym=0
volym=0
area=0

area_eller_volym=input("Area[A] eller Volymen[V] ").upper()
rad=3

if area_eller_volym=="V":
    a=4*3.14*rad*rad*rad
    volym=a/3 
    print(f"Volym: {volym} ")   

elif area_eller_volym=="A":
    area=4*3.14*rad*rad  
    print(f" Area: {area}")