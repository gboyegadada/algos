# @see https://adventofcode.com/2015/day/9

import re
from itertools import permutations

def parse(s: str):
  r = re.match(r'([a-zA-Z]+) to ([a-zA-Z]+) = ([\d]+)', s.strip())

  return (r[1], r[2]), int(r[3])

def find_dist(a: str, b:str, c: dict):
  return c[(a, b)] if (a, b) in c else c[(b, a)]

def calc_route_dist(r: list, c: dict):
  acc = 0
  for i in range(len(r)-1):
    acc += find_dist(r[i], r[i+1], c)

  return acc

def calc_all_route_dists(d: dict):
  # Gather all locations into a set...
  locs = set()
  for (a, b) in d.keys():
    locs.update([a, b])

  # Generate all permutations of the locations i.e. all possible routes
  # ...and calculate total distance in each route
  # We will also filter out reverse routes i.e. a->b->c is the same as c->b->a
  return [calc_route_dist(p, d) for p in permutations(locs, len(locs)) if p <= p[::-1]]

with open('day9_input.txt', 'r') as f: 
  data = dict()
  for l in f:
    k, d = parse(l) 
    data[k] = d

routes = calc_all_route_dists(data)
routes.sort()

print('------------ PART 01 -------------')
print('Distance of the shortest route:', routes[0])

print('\n------------ PART 02 -------------')
print('Distance of the longest route:', routes[-1])
