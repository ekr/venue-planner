#!/usr/bin/env python
import sys

MEETINGS = { 'NONE': 999}
MEETING_LIST = []

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
 
    # Tie breaker: pick least recently used venue
    for m in MEETING_LIST:
        if len(best) == 1:
            return best[0]
        if m in best:
 #           print "Removing %s"%m
            best.remove(m)
        
    die("Internal error")
                
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
        best = pick_venue()
        this_meeting = best
        print "Selecting %s --> %s"%(a[0], best)
        
    if not this_meeting in MEETINGS:
        MEETINGS[this_meeting] = 0
    MEETINGS[this_meeting] +=1
    MEETING_LIST.insert(0, this_meeting)
    
    print a[0], MEETINGS
