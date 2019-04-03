import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

width = 50
height = 50
fig, ax = plt.subplots()
ax.set_xlim([0,width])
ax.set_ylim([0,height])

patches = []
N = 100
ratio = 0.1
ratioInv = 1 - ratio

colors = []

#carré
point = []
point += [[0,0]]
point += [[0, 50]]
point += [[50,50]]
point += [[50,0]]


pt = np.array(point)
polygon = Polygon(pt, True)
patches.append(polygon)

for nb in range(N):
    nPoint = []
    for i in range(len(point) - 1):
        x = ratio * point[i][0] + ratioInv * point[i+1][0]
        y = ratio * point[i][1] + ratioInv * point[i+1][1]
        nPoint += [[ x , y ]]

    x = ratio * point[i+1][0] + ratioInv * point[0][0]
    y = ratio * point[i+1][1] + ratioInv * point[0][1]
    nPoint += [[ x , y ]]
    
    npt = np.array(nPoint)
    polygon = Polygon(npt, True)
    patches.append(polygon)

    point = nPoint

    #ratio += 0.001
    ratioInv = 1 - ratio



p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
p.set_color([1,0,1])


#for i in range(N):
#    if i%2 == 0 :
#       colors += [ 50 ]
#    else:
#        colors += [ 100 ]

for i in range(N):
    colors += [ i ]

p.set_array(np.array(colors))


ax.add_collection(p)

plt.show()




