#from collections import Counter
#import re
#import os
import time

'''     #######     '''

#part 1
def day(te):

    return 0

#part 2
def dayb(te):

    return 0

'''     #######     '''

pva = 2 #which day
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

t = [int(x.strip().replace('<->','').replace(',','').replace('  ',' ')) for x in t]

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
