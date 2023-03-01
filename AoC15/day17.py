# @see https://adventofcode.com/2015/day/17

from lib.helper import filetolist
from itertools import combinations

with open('day17_input.txt', 'r') as f: 
  containers = [int(l) for l in f]

def sum_perm(p: list, cl: list):
    return 150 == sum([cl[i] for i in p])

def calc_num_of_containers(data: list):
  acc = 0
  l = len(data)

  # Generate all combinations of containers
  # ...and only select those volumes that add up to exactly 150l
  # We will also filter out reverse connections i.e. a->b->c is the same as c->b->a
  for dl in range(1, l+1):
    x = [1 for p in combinations(range(l), dl) if p <= p[::-1] and sum_perm(p, data)]
    acc += len(x)

  return acc

print('------------ PART 01 -------------')
print('Number of containers:', calc_num_of_containers(containers))

print('\n------------ PART 02 -------------')

