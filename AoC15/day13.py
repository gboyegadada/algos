# @see https://adventofcode.com/2015/day/13

import re
from itertools import permutations


def parse_line(s: str):
  r = re.match(r'([A-Z][a-z]+) would (gain|lose) ([\d]+) happiness units by sitting next to ([A-Z][a-z]+).', s.strip())

  # Parse happiness change...
  h = int(r[3]) if 'gain' == r[2] else int(r[3]) * -1

  return r[1], r[4], h

with open('day13_input.txt', 'r') as f: 
  hmap = dict()
  for l in f:
    a, b, h = parse_line(l) 
    if a not in hmap:
      hmap[a] = {b: h}
    else:
      hmap[a][b] = h

def calc_happiness_for_arrangement(a: list, hm: dict):
  # Calc happiness change between first and last person
  acc = hm[a[0]][a[-1]] + hm[a[-1]][a[0]]

  # Calc happiness change between everyone in-between
  for i in range(len(a)-1):
    p1, p2 = a[i], a[i+1]
    acc += hm[p1][p2] + hm[p2][p1]

  return acc

def calc_happiness_for_optimal_sitting(hm: dict):
  # Gather everyone into a set...
  names = set(hm.keys())

  # Generate all permutations of sitting arrangements
  # ...and calculate happines change for each person
  # We will also filter out reverse connections i.e. a->b->c is the same as c->b->a
  return max([calc_happiness_for_arrangement(p, hm) for p in permutations(names, len(names)) if p <= p[::-1]])

def add_self(hm: dict):
  me = {}
  for k in hm.keys(): 
    hm[k]['me'] = 0
    me[k] = 0

  hm['me'] = me

  return hm

print('------------ PART 01 -------------')
print('Total change in happiness:', calc_happiness_for_optimal_sitting(hmap))

print('\n------------ PART 02 -------------')
# Add myself to the list
hmap = add_self(hmap)
print('Total change in happiness:', calc_happiness_for_optimal_sitting(hmap))