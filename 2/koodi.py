from collections import Counter
#import re
#import os
import time
'''     #######     '''

''' Part 1 '''
def day(te):
    threes = 0
    twos = 0
    tw = 0
    th = 0
    for t in te:
        c = Counter(t)
        matches = 0
        for i in c.keys():
            if (c[i]) == 2:
                tw += 1
            elif (c[i]) == 3:
                th += 1
        if tw > 0:
            twos += 1
        if th > 0:
            threes += 1
        tw = 0
        th = 0
        #print(twos,threes,twos*threes)
    return twos*threes

''' Part 2 '''
def strdiff(a,b):
    d = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            d += 1
    return d

def strcomm(a,b):
    s = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            s += a[i]
    return s

def dayb(te):
    answ = False

    for t in range(len(te)):
        foo = te[t]
        for i in range(len(te)):
            if t == i:
                continue
            goo = te[i]
            d = strdiff(foo,goo)
            if d == 1:
                print(foo,goo,d)
                com = strcomm(foo,goo)
                return com
    return 0

'''     #######     '''

pva = 2 #which day
dev = 0 # extra prints
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
