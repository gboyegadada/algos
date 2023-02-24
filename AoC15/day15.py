# @see https://adventofcode.com/2015/day/15

import re
from itertools import permutations

def parse_line(s: str):
  r = re.match(r'([A-Za-z]+): capacity ([\-]?[\d]+), durability ([\-]?[\d]+), flavor ([\-]?[\d]+), texture ([\-]?[\d]+), calories ([-]?[\d]+)', s.strip())

  return { 'name': r[1], 'capacity': int(r[2]), 'durability': int(r[3]), 'flavor': int(r[4]), 'texture': int(r[5]), 'calories': int(r[6]) }

with open('day15_input.txt', 'r') as f: 
  ingredients = list()
  for l in f:
    ingredients.append(parse_line(l))

def calc_max_score(i: list, m: tuple):

    # A capacity of 44*-1 + 56*2 = 68
    c = max(0, m[0] * i[0]['capacity'] + m[1] * i[1]['capacity'] + m[2] * i[2]['capacity'] + m[3] * i[3]['capacity'])

    # A durability of 44*-2 + 56*3 = 80
    d = max(0, m[0] * i[0]['durability'] + m[1] * i[1]['durability'] + m[2] * i[2]['durability'] + m[3] * i[3]['durability'])

    # A flavor of 44*6 + 56*-2 = 152
    f = max(0, m[0] * i[0]['flavor'] + m[1] * i[1]['flavor'] + m[2] * i[2]['flavor'] + m[3] * i[3]['flavor']) 

    # A texture of 44*3 + 56*-1 = 76
    t = max(0, m[0] * i[0]['texture'] + m[1] * i[1]['texture'] + m[2] * i[2]['texture'] + m[3] * i[3]['texture']) 

    # cal = max(0, m[0] * i[0]['calories'] + m[1] * i[1]['calories'] + m[2] * i[2]['calories'] + m[3] * i[3]['calories']) 

    return c * d * f * t

score = 0
for p in permutations(range(0, 101), 4):
  if sum(p) != 100: continue

  score = max(score, calc_max_score(ingredients, p))
  

print('Highest score:', score)
