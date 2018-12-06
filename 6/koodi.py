#!/usr/bin/python3

from collections import defaultdict
#import re
#import os
import time
import string
'''     #######     '''

''' Part 1 '''
# (matrix,x-coord,y-coord)
def findClosest(p,r,c):
    vals = [None]*len(p.keys())
    for key in p.keys():
        row = p[key][0]
        col = p[key][1]
        dist = abs(r-row) + abs(c-col)
        vals[int(key[1:])] = dist
        if dist == 0:
            break
    #print(r,c,vals)
    try:
        smallest = min(vals)
    except:
        smallest = 0
    closest = " ."
    if smallest == 0:
        return 0
    id = vals.index(smallest)

    try:
        id2 = vals[(id+1):].index(smallest) + id + 1
    except ValueError:
        #only one minimum
        id2 = None
        closest = " "+str(id)
    return closest

def day(te):
    #import numpy as np
    maxrow = 0
    maxcol = 0
    for i in te:
        maxrow = max(maxrow, int(i[1]))
        maxcol = max(maxcol, int(i[0]))
    #print(maxrow,maxcol)
    d = defaultdict()#np.zeros((maxrow,maxcol,1),dtype=np.int8)
    maxrow += 1
    maxcol += 1

    for i in range(maxrow):
        d[i] = defaultdict(str)
        #for j in range(maxcol):
        #    d[i][j] = "..."
    points = defaultdict(str)
    #add data to matrix
    l = 0
    for i in te:
        r,c = int(i[1]),int(i[0])
        try:
            d[r][c] = "_"+str(l)
        except:
            print(r,c,l,letters[l])
        points["_"+str(l)] = [r,c]
        l += 1

    if 0:
        #print matrix
        for i in range(maxrow):
            row = ""
            for j in range(maxcol):
                p = d[i][j]
                if len(p) == 0:
                    p = " ."
                #row.append(p)
                row += p
            print(row)
    for r in range(maxrow):
        for c in range(maxcol):
            closest = findClosest(points,r,c)
            if closest != 0:
                d[r][c] = closest
    if 0:
        #print matrix
        for i in range(maxrow):
            row = ""
            for j in range(maxcol):
                p = d[i][j]
                if len(p) == 0:
                    p = " ."
                #row.append(p)
                row += p
            print(row)
    area = [0]*len(points.keys())
    ignorepoint = []
    for r in range(maxrow):
        for c in range(maxcol):
            try:
                point = int(d[r][c][1:])
            except ValueError:
                continue
            if point in ignorepoint:
                continue
            if (r in [0, maxrow]) or (c in [0, maxcol]):
                ignorepoint.append(point)
                area[point] = -1
                continue
            area[point] += 1
    #print(ignorepoint)
    #print(max(area), area)
    return max(area)

''' Part 2 '''
def findPoints(p,r,c,limit):
    vals = [0]*len(p.keys())
    for key in p.keys():
        row = p[key][0]
        col = p[key][1]
        dist = abs(r-row) + abs(c-col)
        vals[int(key[1:])] = dist
    largest = sum(vals)
    if largest < limit:
        if min(vals) == 0:
            ans = "#" + str(vals.index(0))
        else:
            ans = " #"
    else:
        ans = 0
    return ans

def dayb(te):
    #import numpy as np
    if samp == 1:
        maxdistance = 32
    else:
        maxdistance = 10000
    maxrow = 0
    maxcol = 0
    for i in te:
        maxrow = max(maxrow, int(i[1]))
        maxcol = max(maxcol, int(i[0]))
    #print(maxrow,maxcol)
    d = defaultdict()#np.zeros((maxrow,maxcol,1),dtype=np.int8)
    maxrow += 1
    maxcol += 1

    for i in range(maxrow):
        d[i] = defaultdict(str)
        #for j in range(maxcol):
        #    d[i][j] = "..."
    points = defaultdict(str)
    #add data to matrix
    l = 0
    for i in te:
        r,c = int(i[1]),int(i[0])
        try:
            d[r][c] = "_"+str(l)
        except:
            print(r,c,l,letters[l])
        points["_"+str(l)] = [r,c]
        l += 1

    if 0:
        #print matrix
        for i in range(maxrow):
            row = ""
            for j in range(maxcol):
                p = d[i][j]
                if len(p) == 0:
                    p = " ."
                #row.append(p)
                row += p
            print(row)
    for r in range(maxrow):
        for c in range(maxcol):
            closest = findPoints(points,r,c,maxdistance)
            if closest != 0:
                d[r][c] = closest
    if 0:
        #print matrix
        for i in range(maxrow):
            row = ""
            for j in range(maxcol):
                p = d[i][j]
                if len(p) == 0:
                    p = " ."
                #row.append(p)
                row += p
            print(row)
    #calculate area
    area = 0
    for r in range(maxrow):
        for c in range(maxcol):
            if "#" in d[r][c]:
                area += 1
    #print(ignorepoint)
    #print(max(area), area)
    return area

'''     #######     '''

pva = 6
dev = 1 # extra prints
part = 1 # 1,2 or 3
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

t = [(x.strip().replace('<->','').replace(',','').replace('  ',' ').split()) for x in t]

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
