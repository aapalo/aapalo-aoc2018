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
    return answer

''' Part 2 '''
def getTime(c):
    return 61 + ord(c) - ord('A')

def dayb(te):
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
    workers = {k: None for k in range(5)}
    i = 0
    seconds = -1
    duration = [ord(x) for x in letters]
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
        checked.add(step)
        if len(available) == 0:
            break
        avail = available.copy()
        step = sorted(avail)[0]
    second = -1
    workers = {k: None for k in range(5)}
    ans = ""
    while (checked) or (any(workers.values())):
        for w in workers:
            if workers[w]:
                #is busy
                letter, step = workers[w]
                if step == getTime(letter):
                    #letter is ready and time is ok
                    for p in prevs:
                        if letter in prevs[p]:
                            prevs[p].remove(letter)
                            #ans += letter
                    #set worker to idle
                    workers[w] = None
                else:
                    workers[w] = (letter, step + 1)
                    #letter not ready, wait one sec
        #print(workers.values())
        for w in workers:
            if not workers[w]:
                #worker idle
                if checked:
                    possib = sorted([x for x in checked if (x not in prevs) \
                    or (len(prevs[x]) == 0)])
                    #print(possib)
                    if possib:
                        letter = possib[0]
                        workers[w] = (letter, 1)
                        checked.remove(letter)
                        ans += letter

        second += 1

    #1265, sample 253
    print("b", (second), ans)
    return second

'''     #######     '''

pva = 7
dev = 0 # extra prints
part = 3 # 1,2 or 3
samp = 2

time0 = time.time()

if samp == 1:
    filename = "/sample.txt"
elif samp == 2:
    filename = "/laurikki.txt"
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
