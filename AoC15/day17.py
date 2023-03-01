# @see https://adventofcode.com/2015/day/17

from itertools import combinations

with open('day17_input.txt', 'r') as f: 
  containers = [int(l) for l in f]

def calc_num_of_ways(c: list):
  min_ways, max_ways = 0, 0
  l = len(c)

  # Generate all combinations of containers
  # Use [combinations of] the index of the list of containers to ensure identical sizes are included
  # ...and only select those volumes that add up to exactly 150 l
  for dl in range(1, l+1):
    ways = [p for p in combinations(range(l), dl) if 150 == sum([c[i] for i in p])]
    lw = len(ways)

    if 0 == min_ways and lw > 0: min_ways = lw

    max_ways += lw

  return max_ways, min_ways

maxw, minw = calc_num_of_ways(containers)

print('------------ PART 01 -------------')
print('Combinations of containers that can exactly fit all 150 liters of eggnog:', maxw)

print('\n------------ PART 02 -------------')
print('Num of ways you can fill the min num of containers that can fit 150 liters:', minw)

