pva = 1

#from collections import Counter
#import re
import os

'''     #######     '''

def day(te):
    return 0

def dayb(te):
    return 1


'''     #######     '''
dev = 1
b = 0
samp = 1

t = ""
if samp == 1:
    with open(str(pva) + "/sample.txt","r") as f:
        t = f.readlines()
elif samp == 0:
    with open(str(pva) + "/input.txt","r") as f:
        t = f.readlines()
t = [x.strip().replace('<->','').replace(',','').replace('  ',' ') for x in t]

if b == 1:
    print(dayb(t))
else:
    print(day(t))
