#!/usr/bin/python3

#from collections import Counter
#import re
#import os
import time
import string

'''     #######     '''

''' Part 1 '''
def day(poly):
    poly = list(poly[0])
    p = 0 #index for poly
    if dev:
        print(poly)
    while p < len(poly):
        try:
            unit0 = poly[p]
            unit1 = poly[p+1]
        except IndexError:
            break
        if unit0 == unit1.swapcase():
            del poly[p:(p+2)]
            if dev:
                print(len(poly), poly)
            p = max(0, p - 1)
            continue
        p += 1
    return len(poly)

''' Part 2 '''
def reactPoly(poly):
    p = 0 #index for poly
    while p < len(poly):
        try:
            unit0 = poly[p]
            unit1 = poly[p+1]
        except IndexError:
            break
        if unit0 == unit1.swapcase():
            del poly[p:(p+2)]
            if dev:
                print(len(poly), poly)
            p = max(0, p - 1)
            continue
        p += 1
    return poly

def dayb(te):
    letters = list(string.ascii_lowercase)
    print(letters)
    d = {}
    for l in letters:
        poly = list(te[0])
        poly[:] = (value for value in poly if value != l)
        poly[:] = (value for value in poly if value != l.upper())

        newpoly = reactPoly(poly)
        d[l] = len(newpoly)
        if dev:
            print(l, len(newpoly), newpoly)
    minpoly = len(list(te[0]))
    minletter = ""
    for l in letters:
        if d[l] < minpoly:
            minletter = l
            minpoly = d[l]
    print(minletter, minpoly)
    return minpoly

'''     #######     '''

pva = 5
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
    print("Part 1: ", day(t))
elif part == 2:
    print("Part 2: ", dayb(t))
elif part == 3:
    #run both
    print("Part 1: ", day(t))
    print("Part 2: ", dayb(t))

tdif = time.time() - time0
print("Elapsed time: {:.4f} s".format(tdif))
