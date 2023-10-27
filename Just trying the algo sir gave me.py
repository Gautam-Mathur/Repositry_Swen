x1 = float(input("Enter the value for x1: "))
x2 = float(input("Enter the value for x2: "))
y1 = float(input("Enter the value for y1: "))
y2 = float(input("Enter the value for y2: "))

dx = x2-x1
dy = y2-y1



def putpixel(x,y):
    dt = 2*(dy - dx)
    ds = 2*dy
    d = (2*dy) - dx
    while x<x2:
        x=x+1
        if d<0:
            d = d+ds
        else:
            y = y+1
            d = d+dy
        print(x1,y1,d,sep=" ")
print ("x  y  d")
putpixel(x1,y1)

        
