from graphics import *

width = 500
height = 500

N = 10



win = GraphWin('Animation', width, height)
win.setBackground('white')

#carré init
vertices = []
vertices += [Point(0,0)]
vertices += [Point(0,height)]
vertices += [Point(width,height)]
vertices += [Point(width,0)]




square = Polygon(vertices)
square.setFill('black')
square.setOutline('black')
square.setWidth(4)  # width of boundary line
square.draw(win)

win.getMouse()
win.close() 


