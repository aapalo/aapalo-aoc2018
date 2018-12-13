#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
#from collections import deque
import numpy as np
'''     #######     '''
def directionDict():
    d = defaultdict(list)
    d["|"] = ["u","d"] # up down
    d[" "] = [] #nothing
    d["-"] = ["l","r"] #left right
    d["+"] = ["u","d","r","l"] #up down left right
    d["\\"] = ["l","d"] #left down
    d["/"] = ["u","r"] #down right
    return d

''' Part 1 '''
def day(te):
    track = defaultdict(dict)
    directions = directionDict()
    col = 0
    row = 0
    for r in range(len(te)):
        track[r] = defaultdict(str)
        for c in range(len(te[r])):
            track[r][c] = te[r][c]
        #track.vstack(t)
        print(t[r])
    print(track.keys(), track[2].values())
    #save cart locations, replace v and ^ with | etc
    #go through the carts, sort by row and then col
    #tick the carts in order
    return 0

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 13
dev = 0 # extra prints
part = 1 # 1,2 or 3
samp = 1 # 0 or 1

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

t = [(x.strip("\n")) for x in t]

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
