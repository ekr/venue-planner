#!/usr/bin/env python
import sys
import re
import math
from optparse import OptionParser


HOME_AIRPORTS_FILE = "home-airports"
DURATIONS_FILE = "durations.txt"

HOME_AIRPORTS = {}
DURATIONS = {}
ATTENDEES = []
AIRPORTS = []
LOCATIONS = ['SFO', 'BOS', 'ARN', 'FRA', 'JFK', 'LHR', 'YYC', 'NYC']
MAX_DURATION = 0


def die(msg):
    print msg
    sys.exit(1)

def dump_urls():
    w = open("locations-urls.html",'w')
    t = open("durations-tmpl.txt", 'w')

    for l in LOCATIONS:
        w.write("<h3>%s</h3>"%l)
        w.write("\n")
        t.write("\n# %s\n"%l)
        for a in AIRPORTS:
            if a == l:
                continue
            w.write('<a href="http://www.kayak.com/#/flights/%s-%s/2012-06-10/2012-06-13/1adults">%s-%s</a><br>'%(a,l,a,l))
            w.write("\n")
            t.write("%s %s\n"%(a,l))

def compute_location_stats(l):
    duration_total = 0
    duration_hist = []
    durations = {}

    for i in range(0,MAX_DURATION + 1):
        duration_hist.append(0)
                   
    for a in ATTENDEES:
        home_airport = HOME_AIRPORTS[a]
        if home_airport == l:
            duration = 0
        elif home_airport == "EWR" and l == "NYC":
            duration = 0
        else:
            route = "%s:%s"%(home_airport, l)
            duration = DURATIONS[route]
        duration_total += duration
        duration_hist[duration] += 1
        durations[a] = duration

    return [round(duration_total / len(ATTENDEES)), duration_hist, durations]


def read_airports():
    # Read home airports file
    f = open(HOME_AIRPORTS_FILE)
    if f is None:
        die("Couldn't open attendees file")
    for l in f:
        l = l.strip()
        args = l.split(" ")
        airport = args.pop()
        if re.match("^[A-Z]+$", airport) is None:
            print "Airport not specified for %s"%" ".join(args).strip()
            continue
    
        attendee = " ".join(args).strip()
        if attendee in HOME_AIRPORTS:
            die("Repeat attendee %s"%attendee)
    
        HOME_AIRPORTS[attendee] = airport
        print "Airport = " + airport
        if not airport in AIRPORTS:
            AIRPORTS.append(airport)
    
    print "All airports (%d) "%(len(AIRPORTS)), AIRPORTS

def read_attendees():
    # Read the attendees list
    f = open(options.attendees)
    if f is None:
        die("Couldn't open attendees file")
    for l in f:
        l = l.strip()
        if not l in HOME_AIRPORTS:
            die("Could not find home airport for %s"%l)
        ATTENDEES.append(l)
    
#dump_urls()

def read_durations():
    global MAX_DURATION
    
    # Read the airport distances
    f = open(DURATIONS_FILE)
    if f is None:
        die("Couldn't open durations file")
    for l in f:
        l = l.strip()
        if l == "":
            continue
        if l == "#DONE":
            break
        if re.match("^#", l):
            continue
        args = l.split(" ")
        if len(args) == 4:
            duration = int(args[2]) + int(args[3])
        elif len(args) == 3:
            duration = int(args[2])
        else:
            die("Bogus line %s"%l)
    
        if duration > MAX_DURATION:
            MAX_DURATION = duration
        DURATIONS["%s:%s"%(args[0], args[1])]=duration
        DURATIONS["%s:%s"%(args[1], args[0])]=duration
    


parser = OptionParser()
parser.add_option('-a', '--attendees', dest='attendees',
                  default='doodle.txt')
parser.add_option('-o', '--output', dest='output',
                  default='output.txt')
parser.add_option('-O', '--hist', dest='hist',
                  default='hist.txt')
(options, args) = parser.parse_args()

read_airports()
read_attendees()
read_durations()

DETAIL = {}
HIST = {}

# Now compute the results
for l in LOCATIONS:
    res = compute_location_stats(l)
    DETAIL[l] = res[2]
    HIST[l] = res[1]
    print "%s %d"%(l, res[0])
    

o = open(options.output, 'w')
if o is None:
    die("Could not open %s"%options.output)

o.write("Attendee")

for l in LOCATIONS:
    o.write("\t%s"%l)
o.write("\n")

for attendee in ATTENDEES:
    o.write(attendee)
    for l in LOCATIONS:
        o.write("\t%d"%(DETAIL[l][attendee]))
    o.write("\n")

o.close()


o = open(options.hist, 'w')
if o is None:
    die("Could not open %s"%options.hist)
o.write("Hours")    
for l in LOCATIONS:
    o.write("\t%s"%l)
o.write("\n")

for i in range(0, MAX_DURATION + 1):
    o.write("%d"%i)
    for l in LOCATIONS:
        o.write("\t%s"%HIST[l][i])
    o.write("\n")



        

    
