#from collections import Counter
#import re
#import os
import time
'''     #######     '''

''' Part 1 '''
def day(te):
    d = {}
    if samp == 1:
        matc = 11
        matr = 9
    else:
        matc = 1000
        matr = 1000
    for r in range(matr):
        d[r] = {}
        for c in range(matc):
            d[r][c] = "."
    xCount = 0
    for i in te:
        t = i.replace("#","").replace("x"," ").replace(":"," ").replace(","," ").split()
        # ['1', '@', '1', '3', '4', '4']
        startR = int(t[3])
        startC = int(t[2])
        rows = int(t[5])
        cols = int(t[4])
        val = int(t[0])
        for r in range(rows):
            for c in range(cols):
                if d[r+startR][c+startC] == ".":
                    d[r+startR][c+startC] = val
                elif d[r+startR][c+startC] == "X":
                    continue
                else:
                    d[r+startR][c+startC] = "X"
                    xCount += 1
    '''
    for r in range(matr):
        printrow = ""
        for c in range(matc):
            printrow += str(d[r][c])
        print(printrow)
    '''
    return xCount

''' Part 2 '''
def dayb2(te):
    #TODO. Try with numpy.
    return 0

def dayb(te):
    d = {}
    claims = {}
    if samp == 1:
        matc = 11
        matr = 9
    else:
        matc = 1000
        matr = 1000
    for r in range(matr):
        d[r] = {}
        for c in range(matc):
            d[r][c] = "."
    xCount = 0
    for i in te:
        # ['#1', '@', '13:', '4x4']
        t = i.replace("#","").replace("x"," ").replace(":"," ").replace(","," ").split()
        # ['1', '@', '1', '3', '4', '4']
        startR = int(t[3])
        startC = int(t[2])
        rows = int(t[5])
        cols = int(t[4])
        val = (t[0])
        claims[val] = rows*cols
        for r in range(rows):
            for c in range(cols):
                if d[r+startR][c+startC] == ".":
                    d[r+startR][c+startC] = val
                elif d[r+startR][c+startC] == "X":
                    continue
                else:
                    d[r+startR][c+startC] = "X"
                    xCount += 1
    for i in claims.keys():
        cc = 0
        for r in range(matr):
            for c in range(matc):
                try:
                    #print(str(i), d[r][c])
                    if str(i) == d[r][c]:
                        cc += 1
                except:
                    continue
        #print("\t",i,cc,claims[i])
        if cc == claims[i]:
            return i

    for r in range(matr):
        printrow = ""
        for c in range(matc):
            printrow += str(d[r][c])
        print(printrow)

    return 0

'''     #######     '''

pva = 3
dev = 0 # extra prints
part = 2 # 1, 2 or 3
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

#parse input data
t = [(x.strip()) for x in t]

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
