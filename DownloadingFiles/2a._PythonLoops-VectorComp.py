#!/usr/bin/env python

import random
positions = [(random.random(), random.random()) for _ in range(10000000)]

# Benchmarking
#%timeit closest((.5, .5), positions)

# Storage of Geographic-Data (Latt/Longt) in Python-list(of Tuples)
def closest (position, positions):
    x0, y0 = position
    dbest, ibest = None, None
    for i, (x, y) in enumerate(positions):
        d = (x - x0) ** 2 + (y - y0) ** 2
        if dbest is None or d < dbest:
            dbest, ibest = d, i
    return ibest

closest(position = a, positions = b)
