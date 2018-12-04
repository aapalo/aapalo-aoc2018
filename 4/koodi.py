#from collections import Counter
#import re
#import os
import time
from datetime import datetime
from datetime import timedelta
'''     #######     '''

def sortdata(l):
    d = {}
    for i in l:
        #day = i[0].replace("-"," ").replace(":"," ").split()
        day = datetime.strptime(i[0],"%Y-%m-%d %H:%M")
        d[day] = str(i[1]).strip()
    #for key in sorted(d.keys()):
        #(datetime.datetime(1518, 11, 1, 0, 0), 'Guard #10 begins shift')
        #print(key,d[key])
    return d

''' Part 1 '''
def day(d):
    #d = {}
    dm = {} #minutes: [guard, awake]
    ds = {} #guard: sleeptime
    nr = 0
    awake = 1
    tstart = sorted(d.keys())[0]
    tend = sorted(d.keys())[-1]
    key = tstart
    guard = d[key].split()[1]
    ds[guard] = 0
    awake = 1
    while key <= tend:
        if key in d.keys():
            row = d[key].split()
            if len(row) == 2:
                if row[0] == "wakes":
                    awake = 1
                else:
                    awake = 0
            if len(row) == 4:
                guard = row[1]
                awake = 1
                if guard not in ds.keys():
                    ds[guard] = 0
        if awake == 0:
            ds[guard] += 1
        dm[key] = [guard,awake]
        key += timedelta(minutes=1)
        if key.hour == 1:
            key += timedelta(hours=22,minutes=40)
            awake = 1
    #for k in sorted(dm.keys()):
    #    print(k,dm[k])
    maxSleeper = ""
    maxSlept = 0
    for k in sorted(ds.keys()):
        #print(k,ds[k],maxSlept)
        val = int(ds[k])
        if maxSlept < val:
            maxSlept = val
            maxSleeper = k
    print("Most sleepy: ", maxSleeper,ds[maxSleeper])
    minList = [0]*60
    key = tstart
    i = 0
    while i < 60:
        for k in sorted(dm.keys()):
            if int(k.minute) == i:
                if (dm[k][0] == maxSleeper):
                    if (dm[k][1] == 0):
                        minList[i] += 1
        i += 1
    st = max(minList)
    idx = minList.index(st)
    print(st,idx,(int(maxSleeper[1:])))
    return idx*(int(maxSleeper[1:]))

''' Part 2 '''
def dayb(d):
    dm = {} #minutes: [guard, awake]
    ds = {} #guard: sleeptime
    nr = 0
    awake = 1
    tstart = sorted(d.keys())[0]
    tend = sorted(d.keys())[-1]
    key = tstart
    guard = d[key].split()[1]
    ds[guard] = 0
    awake = 1
    while key <= tend:
        if key in d.keys():
            row = d[key].split()
            if len(row) == 2:
                if row[0] == "wakes":
                    awake = 1
                else:
                    awake = 0
            if len(row) == 4:
                guard = row[1]
                awake = 1
                if guard not in ds.keys():
                    ds[guard] = 0
        if awake == 0:
            ds[guard] += 1
        dm[key] = [guard,awake]
        key += timedelta(minutes=1)
        if key.hour == 1:
            key += timedelta(hours=22,minutes=40)
            awake = 1
    #loop guards
    dg = {}
    for g in ds.keys():
        dg[g] = 0
        #loop timestamps
        for k in dm.keys():
            pass
    return 0
    # (117061, 2389, 49)
'''     #######     '''

pva = 4
dev = 0 # extra prints
part = 2 # 1,2 or 3
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
