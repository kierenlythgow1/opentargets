import argparse
import sys
import numpy as np
from opentargets import OpenTargetsClient
ot = OpenTargetsClient()

#This script queries the Open Targets REST API using either a target id or disease id. 
#This returns the maximum, minimum, mean and standard deviations of the association scores. 

__version__ = '0.1'
__date__ = '23Aug2019'
__author__ = 'kieren_lythgow@hotmail.com'


Description = 'version %s, date %s, author %s' %(__version__, __date__, __author__)

Parser = argparse.ArgumentParser(description=Description)

Parser.add_argument('-t', '--target_id',
                      metavar='STRING',
                      dest='target_id',
                      #required=True,
                      help='Please supply gene target id')

Parser.add_argument('-d', '--disease_id',
                      metavar='STRING',
                      dest='disease_id',
                      #required=True,
                      help='Please supply disease target id')

if len(sys.argv[1:])==0:
    Parser.print_help()
    Parser.exit()

Args = Parser.parse_args()
print(Args)

target_id = Args.target_id
disease_id = Args.disease_id

#Checks for a target_id as input
if target_id is not None:
    try:
        target_as = ot.get_associations_for_target(target_id)
        print(target_as)
        l=[]
        print('Target id associations:\n')
        for a in target_as:
            print(a['id'], a['association_score']['overall'])
            l.append(a['association_score']['overall'])
        print('Maximum target id association:', np.max(l))
        print('Minimum target id association:', np.min(l))
        print('Mean target id association:', np.mean(l))
        print('Standard deviation of target id association:', np.std(l))
    
    except ValueError:
        print('Target id not found')

#Checks for a disease id as input
if disease_id is not None:
    try:
        disease_as = ot.get_associations_for_disease(disease_id)
        l=[]
        for a in disease_as:
            print(a['id'], a['association_score']['overall'])
            l.append(a['association_score']['overall'])
        print('Maximum disease id association:', np.max(l))
        print('Minimum disease id association:', np.min(l))
        print('Mean disease id association:', np.mean(l))
        print('Standard deviation of disease id association:', np.std(l))
    
    except ValueError:
       print('Disease id not found')
