venue-planner
=============

Tools for planning meeting venues. There are two tools here:

* `compute-cost.py` -- computes the travel time cost 
  to attend venue(s) for a given mix of attendees 
* `plan-rotation.py` -- plans the rotation for a set of
  future meetings given the constraints of other planned
  meetings


### `compute-cost.py`

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







