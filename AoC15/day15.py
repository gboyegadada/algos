# @see https://adventofcode.com/2015/day/15

import re
from itertools import product

def parse_line(s: str):
  r = re.match(r'([A-Za-z]+): capacity ([\-]?[\d]+), durability ([\-]?[\d]+), flavor ([\-]?[\d]+), texture ([\-]?[\d]+), calories ([-]?[\d]+)', s.strip())

  return { 'name': r[1], 'capacity': int(r[2]), 'durability': int(r[3]), 'flavor': int(r[4]), 'texture': int(r[5]), 'calories': int(r[6]) }

with open('day15_input.txt', 'r') as f: 
  ingredients = list()
  for l in f:
    ingredients.append(parse_line(l))

def calc_score(i: list, m: tuple):
    # capacity
    c = max(0, m[0] * i[0]['capacity'] + m[1] * i[1]['capacity'] + m[2] * i[2]['capacity'] + m[3] * i[3]['capacity'])

    # durability
    d = max(0, m[0] * i[0]['durability'] + m[1] * i[1]['durability'] + m[2] * i[2]['durability'] + m[3] * i[3]['durability'])

    # flavor
    f = max(0, m[0] * i[0]['flavor'] + m[1] * i[1]['flavor'] + m[2] * i[2]['flavor'] + m[3] * i[3]['flavor']) 

    # texture
    t = max(0, m[0] * i[0]['texture'] + m[1] * i[1]['texture'] + m[2] * i[2]['texture'] + m[3] * i[3]['texture']) 

    # calories
    cal = m[0] * i[0]['calories'] + m[1] * i[1]['calories'] + m[2] * i[2]['calories'] + m[3] * i[3]['calories']

    return c * d * f * t, cal

max_score = 0
max_score_caloric = 0

for p in product(range(0, 101), repeat=4):
  if sum(p) != 100: continue

  score, cal = calc_score(ingredients, p)
  max_score = max(score, max_score)

  if 500 == cal and score > max_score_caloric:
    max_score_caloric = score

print('------------ PART 01 -------------')
print('Highest score:', max_score)

print('\n------------ PART 02 -------------')
print('Highest score with a calorie total of 500:', max_score_caloric)
