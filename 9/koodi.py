#!/usr/bin/python3

#from collections import Counter
#import re
#import os
from collections import deque
from collections import defaultdict
import time
'''     #######     '''

''' Part 1 '''
def day(te):
    #print(te.split())
    score = defaultdict(int)
    players = int(te.split()[0])
    lastMarble = int(te.split()[-2])
    if part == 2:
        lastMarble *= 100
    p = deque([0])
    cm = 0 #current marble
    for m in range(1, lastMarble + 1):
        if m % 23 != 0:
            #not a multiple of 23
            p.rotate(-1)
            p.append(m)
        else:
            #multiple of 23
            player = m % players #current player
            p.rotate(7)
            m7 = p.pop() #rotate 7 steps ccw and pop
            score[player] += m + m7
            p.rotate(-1) #current marble

        #print(m % players, p)
    ans = max(score.values())
    #print(score.keys(), score.values())

    return ans

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 9
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

if part == 1:
    if samp:
        correct = deque([32, 8317, 146373, 2764, 54718, 37305])
        for i in t:
            ans = day(i)
            corr = correct.popleft()
            print("Part 1: {} == {}: \t{}".format(ans, corr, ans == corr))
    else:
        print("Part 1: ", day(t[0]))
elif part == 2:
    print("Part 2: ", day(t[0]))
elif part == 3:
    #run both
    print("Part 1: ", day(t))
    print("Part 2: ", dayb(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
