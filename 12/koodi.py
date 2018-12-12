#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
#from collections import deque
'''     #######     '''

''' Part 1 '''
def sumList(l):
    s = 0
    #sum of the numbers of pots containing a plant
    for i in range(len(l)):
        if l[i] == "#":
            s += i
    return s

def printList(l):
    r = "".join(l)
    return r

def day(te):
    initialState = (te[0].split(":"))[1].strip()
    #print(initialState)
    pots = []
    potlen = len(initialState)
    rules = {}
    for p in initialState:
        pots.append(p)
    for r in te[1:]:
        row = r.split()
        if len(row) != 3:
            continue
        #print(row[0],row[1],row[2])
        rules[row[0]] = row[2]
    print("".join(pots))
    for loops in range(20):
        for i in range(2,potlen-2):
            k = "".join(pots[(i-2):(i+3)])
            if k in rules.keys():
                pots[i] = rules[k]
        print("{} loops: {}".format(loops,"".join(pots)))
    print(sumList(pots))
    print("OBS: oikea lista ei ala 0-indeksistä.")
    return 0

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 12
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
