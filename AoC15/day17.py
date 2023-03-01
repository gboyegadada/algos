# @see https://adventofcode.com/2015/day/17

from itertools import combinations

with open('day17_input.txt', 'r') as f: 
  containers = [int(l) for l in f]

def sum_perm(p: list, cl: list):
    return 150 == sum([cl[i] for i in p])

def calc_num_of_containers(data: list):
  min_ways, max_ways = 0, 0
  l = len(data)

  # Generate all combinations of containers
  # ...and only select those volumes that add up to exactly 150l
  # We will also filter out reverse connections i.e. a->b->c is the same as c->b->a
  for dl in range(1, l+1):
    ways = [p for p in combinations(range(l), dl) if p <= p[::-1] and sum_perm(p, data)]
    lw = len(ways)

    if 0 == min_ways and lw > 0: min_ways = lw

    max_ways += lw

  return max_ways, min_ways

maxw, minw = calc_num_of_containers(containers)

print('------------ PART 01 -------------')
print('Combinations of containers that can exactly fit all 150 liters of eggnog:', maxw)

print('\n------------ PART 02 -------------')
print('Num of ways you can fill the min num of containers that can fit 150 liters:', minw)

