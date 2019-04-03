import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(50, 50)

#
ax = plt.axes(xlim=(0, 50), ylim=(0, 50))
patch = plt.Circle((5, -5), 0.75, fc='y')

points = [[2, 1], [8, 1], [8, 4]]
polygon = plt.Polygon(points)
ax.add_patch(patch)
#

N = 100
ratio = 0.1
ratioInv = 1 - ratio
polygons = []

#carré
poly = []
poly += [[0,0]]
poly += [[0, 50]]
poly += [[50,50]]
poly += [[50,0]]


for nb in range(N):
    polyIns = []
    for i in range(len(poly) - 1):
        x = ratio * poly[i][0] + ratioInv * poly[i+1][0]
        y = ratio * poly[i][1] + ratioInv * poly[i+1][1]
        polyIns += [[ x , y ]]

    x = ratio * poly[i+1][0] + ratioInv * poly[0][0]
    y = ratio * poly[i+1][1] + ratioInv * poly[0][1]
    polyIns += [[ x , y ]]

    poly = polyIns

    polygons += [[[poly]]]

    #ratio += 0.001
    ratioInv = 1 - ratio











def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    #
    
    
    
    
    return patch,

def animate(i):
    #carré
    poly = []
    poly += [[0,0]]
    poly += [[0, 50]]
    poly += [[50,50]]
    poly += [[50,0]]
    
    points = [[2, 1], [8, 1], [8, 4]]
    polygon = plt.Polygon(poly)
    ax.add_patch(polygon)

    return polygon,




anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)

plt.show()
