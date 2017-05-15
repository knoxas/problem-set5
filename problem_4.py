#/usr/bin/env python3

#set-up
import sys
filename = sys.argv[1]

from collections import Counter
from pysam import AlignmentFile

bamfile = AlignmentFile(filename)

count = 0
strands = Counter()
mismatches = Counter()

#count positive and negative strand alignments; identified using the flag
# tag for the strands
for record in bamfile:
    strand = record.flag
    strands[strand] += 1
for strand, count in strands.items():
    if strand == 0:
        print("Positive strand alignments:", count)
    if strand == 16:
        print("Negative strand alignments:", count)

#count the number of mismatches using the NM tag
#this section of code doesn't print answers when this script is run, but
# the code works when I run it directly in the python line
for record in bamfile:
    nm = record.get_tag('NM')
    mismatches[nm] += 1
for nm, count in mismatches.items():
    if nm == 0:
        print("Total number of alignments with no mismstches:", count)
    elif nm != 0:
        global counts
        counts += count
        print("Total number of alignments with >0 mismatches:", counts)
