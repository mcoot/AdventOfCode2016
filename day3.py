from typing import Tuple
from itertools import chain
import math


def is_valid(sides: Tuple[int]) -> bool:
    if sides[0] + sides[1] <= sides[2]:
        return False
    if sides[0] + sides[2] <= sides[1]:
        return False
    if sides[1] + sides[2] <= sides[0]:
        return False
    return True


doPartB = True
valid = 0

with open('inputs/day3.txt', 'r') as f:
    raw_values = ''.join(list(chain(*(f.readlines())))).replace('\n',' ').split()

if doPartB:
    # Group the values into groups of 9 values (3 triangles)
    values = [raw_values[9 * i:9 * i + 9] for i in range(0, math.floor(len(raw_values) / 9))]
    # For each group of 9 values, create triangle tuples from the columns
    triangles = [[(int(section[i+0]), int(section[i + 3]), int(section[i + 6]))
                  for i in range(0, math.floor((len(section)) / 3))]
                 for section in values]
    # Flatten the list of lists of triangles
    triangles = list(chain(*triangles))
else:

    triangles = list(zip(raw_values[::3], raw_values[1::3], raw_values[2::3]))

for triangle in triangles:
    if is_valid(triangle):
        valid += 1

print("Valid: %d/%d" % (valid, len(triangles)))
