# @see https://adventofcode.com/2015/day/12

import json

with open('day12_input.txt', 'r') as f: 
  doc = json.loads(f.readline())

def calc_balance(d, acc: int = 0):
  if type(d) == int:
    acc += d
  elif type(d) == str:
    pass
  elif type(d) == list:
    for v in d:
        acc = calc_balance(v, acc)
  elif type(d) == dict:
    for v in d.values():
        acc = calc_balance(v, acc)

  return acc 

def calc_balance_sans_red(d, acc: int = 0):
  if type(d) == int:
    acc += d
  elif type(d) == str:
    pass
  elif type(d) == list:
    for v in d:
        acc = calc_balance_sans_red(v, acc)
  elif type(d) == dict and 'red' not in d.values():
    for v in d.values():
        acc = calc_balance_sans_red(v, acc)

  return acc 

print('------------ PART 01 -------------')
print('Balance:', calc_balance(doc))

print('\n------------ PART 02 -------------')
print('Balance:', calc_balance_sans_red(doc))