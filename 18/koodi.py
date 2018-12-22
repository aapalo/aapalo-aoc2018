#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
#from collections import deque
'''     #######     '''

def listNeighbors(r,c,acres):
    grounds = 0 # "."
    trees = 0   # "|"
    yards = 0   # "#"
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if (j == 0) and (i == 0):
                continue
            try:
                val = (acres[r+j][c+i])
            except KeyError:
                continue
            if val == ".":
                grounds += 1
            elif val == "|":
                trees += 1
            elif val == "#":
                yards += 1
    return [grounds,trees,yards]

def printAcres(acres):
    for r in acres.keys():
        row = ""
        for c in acres[r].keys():
            row += acres[r][c]
        print(row)
    return 0

def updateAcres(oldAcres):
    newAcres = defaultdict(dict)
    for row in range(rows):
        newAcres[row] = defaultdict(str)
        for col in range(cols):
            newAcres[row][col] = oldAcres[row][col]
    #print(newAcres[0].keys())
    for row in range(rows):
        for col in range(cols):
            a = oldAcres[row][col]
            if a == ".":
                if listNeighbors(row,col,oldAcres)[1] >= 3:
                    newAcres[row][col] = "|"
            elif a == "|":
                if listNeighbors(row,col,oldAcres)[2] >= 3:
                    newAcres[row][col] = "#"
            elif a == "#":
                neighb = listNeighbors(row,col,oldAcres)
                if (neighb[2] >= 1) and (neighb[1] >= 1):
                    newAcres[row][col] = "#"
                else:
                    newAcres[row][col] = "."
    return newAcres

def countResources(acres):
    woods = 0
    yards = 0
    for row in range(rows):
        for col in range(cols):
            if acres[row][col] == "|":
                woods += 1
            elif acres[row][col] == "#":
                yards += 1
    return (woods*yards)

def day(te,loops):
    row = 0
    d = defaultdict(dict)
    for t in te:
        d[row] = defaultdict(str)
        for col in range(len(t)):
            d[row][col] = t[col]
        row += 1
    #printAcres(d)
    vals = []
    if loops == 10:
        for i in range(1,(loops+1)):
            d = updateAcres(d)
        return countResources(d)
    else:
        #repeats every 28 steps
        idx = []
        vals = []
        '''
        for i in range(1,(loops+1)):
            d = updateAcres(d)
            if i > 2000:
                idx.append(i)
                vals.append(countResources(d))
                print(i,vals[-1])
                if i > 2050:
                    break
        '''
        idx = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]
        vals = [169260, 169524, 168935, 173952, 179622, 180299, 188155, 195776, 192198, 199076, 206375, 210576, 208658, 212520, 213395, 216660, 210368, 203794, 195510, 180873, 177126, 176320, 167862, 169218, 170428, 172898, 169470, 165780]
        print(vals[int(loops-2001)%28])

    return countResources(d)

'''     #######     '''

pva = 18
dev = 0 # extra prints
part = 2 # 1,2 or 3
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
rows = len(t)
cols = len(t[0])
print(rows,cols)
if part == 1:
    print("Part 1: ", day(t,10))
elif part == 2:
    print("Part 2: ", day(t,1000000000))
elif part == 3:
    #run both
    print("Part 1: ", day(t,10))
    print("Part 2: ", day(t,1000000000))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
