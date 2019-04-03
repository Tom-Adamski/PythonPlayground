from graphics import *
import time

###################################################

width = 600
height = 600
N = 1000
ratio = 0.01
b = 0
ratioAug = 0
#ratioAug = -0.0001

####################################################

def calcPointEntre(poly,a,b,ratio):
    ratioInv = 1 - ratio
    x = poly[a].getX() * ratio + poly[b].getX() * ratioInv
    y = poly[a].getY() * ratio + poly[b].getY() * ratioInv
    return Point(x,y)


def drawPolyBW(vertices,win,b):
    poly = Polygon(vertices)
    if b==0:
        poly.setFill('black')
        poly.setOutline('black')
    else:
        poly.setFill('white')
        poly.setOutline('white')
    poly.setWidth(4)
    poly.draw(win)

        
    
#####################################################




win = GraphWin('Animation', width, height)
win.setBackground('white')

# square init
vertices = [ Point(0,0), Point(0,height), Point(width,height), Point(width,0)]

# triangle init
vertices = [ Point(0,0), Point(width/2,height),Point(width,0)]

# rotated triangle init
vertices = [ Point(0,height/2), Point(width/2,height),Point(width,height/2),Point(width/2,0)]


print(vertices)
drawPolyBW(vertices,win,b)


for nb in range(N):
    b = 1-b
    nVert = []
    for i in range(len(vertices)-1):
        vert = calcPointEntre(vertices,i,i+1,ratio)
        nVert += [vert]
     
    vert = calcPointEntre(vertices,i+1,0,ratio)
    nVert += [vert]
    drawPolyBW(nVert,win,b)
    
    vertices = nVert
    ratio += ratioAug

    time.sleep(0)
    
##



win.getMouse()
win.close() 




