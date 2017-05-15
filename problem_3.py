# /usr/bin/env python3

#set-up
import sys

filename = sys.argv[1]

from collections import Counter

count = 0

#define counters for finding 5' and 3' hexamers
hexamer_5 = Counter()
hexamer_3 = Counter()

#code for parsing fastq files
for line in open(filename):
    line = line.rstrip()

    if count == 0:
        name = line
        count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0

        hexamers_5 = []
        hexamer_L_5 = seq[0:6]
        hexamer_5[hexamer_L_5] =+ 1
        hexamers_3 = []
        hexamer_L_3 = seq[-6:]
        hexamer_3[hexamer_L_3] += 1

for key, value in hexamer_5.items():
    sortme = [(v,k) for k,v in hexamer_5.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("Most common 5' hexamer:", sortme[0][1])
        
for key, value in hexamer_3.items():
    sortme = [(v,k) for k,v in hexamer_3.items()]
    sortme
    sortme.sort()
    sortme.reverse()
print("Most common 3' hexamer:", sortme[0][1])
