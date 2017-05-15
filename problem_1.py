#/usr/bin/env python3

from collections import Counter

counts = Counter()

import sys

filename = sys.argv[1]

for line in open(filename):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chrom = fields[0]
    counts[chrom] += 1
for chrom, count in counts.items():
    print(chrom, count, sep = '\t')

