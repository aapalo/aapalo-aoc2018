#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
from collections import defaultdict
#from collections import deque
'''     #######     '''

''' Part 1 '''
def calcPower(x,y,s):
    rackID = 10 + x
    ans = rackID * y
    ans += s #serial
    ans *= rackID
    #hundreds, or 0 if <100
    ans -= 5
    return ans

def day(te):
    serial = int(te[0])
    d = defaultdict(list)
    for k in range(1,301):
        d[k] = defaultdict(int)
    print(len(d.keys()))
    return 0

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 11
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
