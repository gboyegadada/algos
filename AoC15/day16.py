# @see https://adventofcode.com/2015/day/16

import re

MFCSAM_output = {
  'children': 3,
  'cats': 7,
  'samoyeds': 2,
  'pomeranians': 3,
  'akitas': 0,
  'vizslas': 0,
  'goldfish': 5,
  'trees': 3,
  'cars': 2,
  'perfumes': 1
}

def parse_line(s: str):
  # Sue 1: children: 1, cars: 8, vizslas: 7
  r = re.match(r'Sue ([\d]+): ([a-z]+): ([\d]+), ([a-z]+): ([\d]+), ([a-z]+): ([\d]+)', s.strip())

  return int(r[1]), {r[2]: int(r[3]), r[4]: int(r[5]), r[6]: int(r[7])}

with open('day16_input.txt', 'r') as f: 
  aunts = list()
  for l in f:
    aunts.append((parse_line(l)))

def compare_exact(o: dict, s: dict):
  matches = 0
  for k, v in s.items():
    if v == o[k]:
      matches += 1

  return len(s) == matches

def compare_inexact(o: dict, s: dict):
  matches = 0
  for k, v in s.items():
    # the cats and trees readings indicates that there are greater than that many...
    if k in ('trees', 'cats') and v > o[k]:
      matches += 1

    # the pomeranians and goldfish readings indicate that there are fewer than that many...
    elif k in ('pomeranians', 'goldfish') and v < o[k]:
      matches += 1

    # others entries exact...
    elif k not in ('pomeranians', 'goldfish', 'trees', 'cats') and v == o[k]:
      matches += 1

  return 3 == matches


def part_one(o: dict, a: list):
  res = None
  for i, s in a:
    if compare_exact(o, s):
      res = i
      break

  return res

def part_two(o: dict, a: list):
  res = None
  for i, s in a:
    if compare_inexact(o, s):
      res = i
      break

  return res


print('------------ PART 01 -------------')
print('Found: Sue', part_one(MFCSAM_output, aunts))

print('\n------------ PART 02 -------------')
print('Found: Sue', part_two(MFCSAM_output, aunts))
