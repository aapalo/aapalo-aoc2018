#!/usr/bin/python3

#from collections import Counter
#import re
#import os
from collections import defaultdict
import matplotlib.pyplot as plt
import time
'''     #######     '''

''' Part 1 '''
def getPoints(p):
    #input position dict, output two lists: xpos and ypos for each point
    xpos = []
    ypos = []
    for k in p.keys():
        xpos.append(p[k][0])
        ypos.append(p[k][1])
    return [xpos, ypos]

def getArea(p):
    #into how large of an area do all the points fit
    [x,y] = getPoints(p)
    return (max(x)-min(x))*(max(y)-min(y))

def plotMat(p,idx):
    [x,y] = getPoints(p)
    #plt.plot(x,y,'x')
    plt.clf()
    plt.scatter(x,y)
    #plt.savefig('d10-s-{}.png'.format(idx))


def printMat(p):
    [x,y] = getPoints(p)
    for i in range(max(y),min(y)):
        row = ["."]*(max(x)-min(x))
        for j in range(min(x),max(x)):
            if [i,j] in p.values():
                row[j-min(x)]= "#"

        print("".join(row))
    return 0

def day(te):
    pos = defaultdict() #positions
    vel = defaultdict() #velocities
    i = 0 #point ID
    for t in te:
        [_,x,y,_,vx,vy] = (t.replace("<", " ").replace(">", " ").split())
        [x,y,vx,vy] = [int(x),int(y),int(vx),int(vy)]
        #print([x,y,vx,vy])
        pos[i] = [x,y]
        vel[i] = [vx,vy]
        i += 1
    #print(pos.keys())
    #print(pos.values())
    j = 0
    area = getArea(pos)
    print(area)
    printed = False
    while 1:
        for k in pos.keys():
            [x,y] = pos[k]
            [vx,vy] = vel[k]
            pos[k] = [x+vx,y+vy]
        newArea = getArea(pos)
        if newArea < 10000:
            plotMat(pos,j)
            printed = True
            if j == 10075:
                printMat(pos)
                plt.show()
        elif (newArea > 10000) and printed:
            break

        j+= 1
    return 0

''' Part 2 '''
def dayb(te):
    #return 10075
    return 10075+1

'''     #######     '''

pva = 10
dev = 0 # extra prints
part = 3 # 1,2 or 3
samp = 0 # 0 or 1

time0 = time.time()

if samp == 1:
    filename = "/sample.txt"
else:
    filename = "/input.txt"

try:
    with open(str(pva) + filename,"r") as f:
        t = f.readlines()
except FileNotFoundError:
    with open("." + filename,"r") as f:
        t = f.readlines()

t = [(x.strip().replace('<->','').replace(',','').replace('  ',' ')) for x in t]

if part == 1:
    print("Part 1: ", day(t))
elif part == 2:
    print("Part 2: ", dayb(t))
elif part == 3:
    #run both
    print("Part 1: ", day(t))
    print("Part 2: ", dayb(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
