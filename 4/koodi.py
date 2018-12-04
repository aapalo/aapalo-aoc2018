#from collections import Counter
#import re
#import os
import time
from datetime import datetime
'''     #######     '''

def sortdata(l):
    d = {}
    retL = []
    alldates = []
    for i in l:
        #day = i[0].replace("-"," ").replace(":"," ").split()

        day = datetime.strptime(i[0],"%Y-%m-%d %H:%M")
        alldates.append(day)
        d[day] = i
    for i in sorted(alldates):
        retL.append(d[i])
        #d[l[0]]
    #print(retL)
    return(retL)

''' Part 1 '''
def day(te):
    d = {}
    nr = 0
    awake = 1
    for t in te:
        row = t[0].split()
        row.append(t[1].split())
        print(row)
        if len(t) == 4:
            if nr == 0:
                continue
            #['1518-11-01', '00:05', 'falls', 'asleep'] 4
            day,ti,action,foo = t
            if action == "falls":
                if awake == 1:
                    tiSleep = int(ti[3:])
                awake = 0
            elif action == "wakes":
                if awake == 0:
                    tiWake = int(ti[3:])
                    d[nr] += tiWake - tiSleep
                awake = 1

        elif len(t) == 6:
            day,ti,guard,nr,act,foo = t
            #['1518-11-01', '00:00', 'Guard', '#10', 'begins', 'shift'] 6
            #print(t)
            awake = 1
            if nr not in d.keys():
                d[nr] = 0
    maxSleep = 0
    maxSleeper = ""
    for i in d.keys():
        if d[i] > maxSleep:
            maxSleeper = i
        print(i,d[i])
    print(len(d.keys()))
    return maxSleeper

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 4
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
t = [(x.strip()).replace("[","").split("]") for x in t]
t = sortdata(t)
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
