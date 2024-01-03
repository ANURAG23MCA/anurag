from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere
#using rectangle module
l=int(input("enter length"))
w=int(input("enter width")) 
print("area of rectangle=",rectangle.area(l,w))
print("perimter of reactangle=",rectangle.perimter(l,w))
#using circle module
r=int(input("enter radius"))
print("area of circle=",circle.area(r))
print("perimeter of circle=",circle.perimeter(r))
#using cuboid module
l=int(input("enter length"))
w=int(input("enter width"))
h=int(input("enter height"))
print("surfacearea of cuboid=",cuboid.surfacearea(l,w,h))
print("volume of cuboid=",cuboid.volume(l,w,h))
#using sphere module
r=int(input("enter radius"))
print("surfacearea of sphere=",sphere.surfacearea(r))
print("volume of sphere=",sphere.volume(r))
