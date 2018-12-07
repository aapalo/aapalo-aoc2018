#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
import string
from collections import defaultdict
'''     #######     '''

''' Part 1 '''
def day(te):
    letters = list(string.ascii_uppercase)
    prevs = defaultdict(set) #prevs[A] = [C]
    nexts = defaultdict(set) #nexts[A] = [B,D]
    for t in te:
        prev = t.split(" ")[1]
        next = t.split(" ")[7]
        prevs[next].add(prev)
        nexts[prev].add(next)
        #print(prev,ord(prev),next,ord(next))
    #find start and end steps
    firstStep = set()
    lastStep = set()
    for l in letters:
        if (l in prevs.keys()) or (l in nexts.keys()):
            if (l not in prevs.keys()):
                firstStep.add(l)
            if (l not in nexts.keys()):
                lastStep.add(l)
            #print(l,prevs[l],nexts[l])
    #print(firstStep,sorted(firstStep))
    #print(lastStep)
    available = firstStep
    avail = available.copy() #subet of available
    answer = ""
    checked = set()
    step = sorted(available)[0]
    i = 0
    while len(available) > 0:
        if dev:
            print(step, sorted(available),len(available), answer)
        if step in answer:
            available.remove(step)
            avail = available.copy()
            step = sorted(avail)[0]
            continue
        if not (prevs[step] <= checked):
            avail.remove(step)
            step = sorted(avail)[0]
            continue
            #not a subset of checked

        #    continue
        available.remove(step)
        available |= nexts[step] #add smaller set to available
        answer += step
        if len(available) == 0:
            break
        checked.add(step)
        avail = available.copy()
        step = sorted(avail)[0]
    #for each step, add all availables in a list
    #go through availables in alphabetical order

    '''
        for tasks in available:
            if ord(a) < ord(b):
                do_stuff_with(a)
                pop(a)
    '''

    return answer

''' Part 2 '''
def dayb(te):

    return 0

'''     #######     '''

pva = 7
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
