# opentargets

This script queries the Open Targets REST API using either a target id or disease id. 
This returns the maximum, minimum, mean and standard deviations of the association scores.

# requirements
Numpy
Opentargets

# command line
usage: otquery.py [-h] [-t STRING] [-d STRING]

version 0.1, date 23Aug2019, author kieren_lythgow@hotmail.com

optional arguments:
  -h, --help            show this help message and exit
  -t STRING, --target_id STRING
                        Please supply gene target id
  -d STRING, --disease_id STRING
                        Please supply disease target id
