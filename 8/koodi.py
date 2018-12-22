#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
from collections import deque
'''     #######     '''

''' Part 1 '''
def day(te):
    dm = defaultdict(set) #node metadata
    dmlen = defaultdict(int) #node metadata amount
    dc = defaultdict(deque) #node childs
    dclen = defaultdict(int) #node child amount

    childs = 0 #how many child nodes in node, unused
    mdatas = 0 #how many metadata entries in node, unused

    nodes = deque() #list of to-do nodes
    node = 0
    #first node:
    dclen[node] = te[0]
    dmlen[node] = te[1]
    dc[node].append(te[2])
    
    i = 3
    while i < len(te):
        if len(nodes):
            node = nodes.popleft()
        print(node, nodes)
        if len(dc[node]) == dclen[node]:
            #all needed childs in node
            if len(dm[node]) < dmlen[node]:
                dm[node].add(t) #add metadata
            else:
                nodes.append(t)
            continue
        else:
            #if childs remaining
            nodes.appendleft(t)
        i += 1
    print(dm.keys())
    print(dm.values())

    return 0

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 8
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

t = [(x.strip().replace('<->','').replace(',','').replace('  ',' ').split()) for x in t]
t = [int(x) for x in t[0]]

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
