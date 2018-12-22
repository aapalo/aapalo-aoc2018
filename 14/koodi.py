#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
#from collections import defaultdict
from collections import deque

'''     #######     '''

''' Part 1 '''
def day(te):
    rec = deque([3,7])
    first = 0
    second = 1
    while len(rec) < te + 10:
        rsum = rec[first]+rec[second]
        if rsum > 9:
            sc1 = int(rsum / 10)
            sc2 = rsum % 10
            rec.append(sc1)
            rec.append(sc2)
        else:
            rec.append(rsum)
        first = (first + rec[first] + 1) % len(rec)
        second = (second + rec[second] + 1) % len(rec)
        #print(i, rec,rsum, sc1, sc2)
    ret = (list(rec)[te:te+10])
    ret = "".join([str(x) for x in ret])
    return ret

''' Part 2 '''
def dayb(te):
    rec = "37"
    first = 0
    second = 1
    te = str(te)
    telen = len(te) + 1
    while te not in rec[-telen:]:
        rec += str(int(rec[first]) + int(rec[second]))

        first = (first + int(rec[first]) + 1) % len(rec)
        second = (second + int(rec[second]) + 1) % len(rec)
        #print(rec, b)

    return str(rec.index(te))

'''     #######     '''

pva = 14
dev = 0 # extra prints
part = 2 # 1,2 or 3
samp = 0 # 0 or 1

time0 = time.time()

if samp:
    if part == 1:
        t = [5,18,2018]
        answers = ["0124515891", "9251071085", "5941429882"]
    elif part == 2:
        t = ["51589","01245","92510","59414"]
        answers = ["9","5","18","2018"]
else:
    t = [825401]

if part == 1:
    if samp:
        for i in range(len(t)):
            ans = day(t[i])
            print("{}, {}, correct: {}".format(ans, (answers[i]), ans==(answers[i])))
    else:
        print("Part 1: ", day(t[0]))
elif part == 2:
    if samp:
        for i in range(len(t)):
            ans = dayb(t[i])
            print("{}, {}, correct: {}".format(ans, (answers[i]), ans==(answers[i])))

    else:
        print("Part 2: ", dayb(t[0]))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
