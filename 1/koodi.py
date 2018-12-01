

#from collections import Counter
#import re
#import os
import time
'''     #######     '''

#part 1
def day(te):
    sum = 0
    for t in te:
        sum += t
    return sum

#part 2
def dayb(te):
    sum = 0
    lsum = []
    ans = False
    while(1):
        for t in te:
            #print(l)
            sum += t
            if sum in lsum:
                ans = True
                break
            lsum.append(sum)
        if ans == True:
            break
    #print(len(lsum),sum)
    return sum

#part 2, with set()
def dayb2(te):
    sum = 0
    lsum = set()
    ans = False
    while(1):
        for t in te:
            #print(l)
            sum += t
            if sum in lsum:
                ans = True
                break
            lsum.add(sum)
        if ans == True:
            break
    #print(len(lsum),sum)
    return sum

'''     #######     '''
pva = 1
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

t = [int(x.strip().replace('<->','').replace(',','').replace('  ',' ')) for x in t]

if part == 1:
    print("Part 1: ", day(t))
elif part == 2:
    print("Part 2: ", dayb2(t))
elif part == 3:
    #run both
    print("Part 1: ", day(t))
    print("Part 2: ", dayb(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
