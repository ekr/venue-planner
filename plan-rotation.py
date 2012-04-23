#!/usr/bin/env python
import sys

MEETINGS = { 'NONE': 999}

VENUES = ["EU", "WC", "EC"]

def die(msg):
    print msg
    sys.exit(1)

def pick_venue():
    best = ['NONE']

    for v in VENUES:
        if not v in MEETINGS:
            count = 0
        else:
            count = MEETINGS[v]
        
        if MEETINGS[best[0]] > count:
            best = [v]
        elif MEETINGS[best[0]] == count:
            best.append(v)

    print "Best venues: ",
    print best
    
    return best
                
f = open(sys.argv[1])
for l in f:
    l = l.strip()
    if l == "":
        continue
    a = l.split(" ")
    if len(a) != 2:
        die("Bogus line %s"%l)
    
    if a[1] != "XX":
        this_meeting = a[1]
    else:
        order = pick_venue()
        this_meeting = order[0]
        print "Selecting %s --> %s"%(a[0], order[0])
        
    if not this_meeting in MEETINGS:
        MEETINGS[this_meeting] = 0
    MEETINGS[this_meeting] +=1
    
    print a[0], MEETINGS
