venue-planner
=============

Tools for planning meeting venues. There are two tools here:

* `compute-cost.py` -- computes the travel time cost 
  to attend venue(s) for a given mix of attendees 
* `plan-rotation.py` -- plans the rotation for a set of
  future meetings given the constraints of other planned
  meetings


### Computing Venue Costs

`compute-cost.py` needs three inputs:

* a durations file listing the travel times between any pair of airports
  (expresses as three letter codes). Must be named `durations.txt
* a home airports file listing the home airports for every potential attendee.
  Must be names `home-airports.txt`
* an attendees file listing the actual attendees. By default 
  `doodle-respondees.txt` but can be specified with `-a`

The list of candidate venues is hardcoded at the top of the file.

The output (by default in `output.txt`) is a table of the cost for each
venue for each attendee. stdout also contains some simple summary statistics
for each venue.


### Planning Meetings

`plan-rotation.py` is designed to plan a "fair" (even) rotation of
meetings between a set of regions (currently EU (Europe), WC (West
Coast US) and EC (East Coast US)). It takes a single input, the list
of planned meetings in order. For each meeting without a location, it
assigns a region attempting to pick the least used region. Ties
are broken by the least-recently visited region.

The input file consists of pairs of meeting name and region 
specified on a single line, like:

IETF84 WC
INT84.5 XX

Any meetings with region XX is filled in with the currently "next" 
region based on previous meetings. Any other regions are stored
but basically ignored.

