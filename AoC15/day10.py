# @see https://adventofcode.com/2015/day/10

import re

data = '1113122113'

def step(n: str):
  m = re.findall(r'([1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+|[0]+)', n)

  nxt = ''
  for s in m:
    nxt += str(len(s)) + s[0]

  return nxt

def seq(d: str, steps: int):
  for _ in range(steps):
    d = step(d)

  return d

print('------------ PART 01 -------------')
num = seq(data, 40)
print('The length of the result after 40 steps:', len(num))

print('\n------------ PART 02 -------------')
num = seq(num, 10)
print('The length of the result after 50 steps:', len(num))