import sys
import re

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

data = []
for l in open(f):
  data.append(l.strip())


def is_valid(entry):
  m = re.search('(\d+)-(\d+) (.): (.*)', entry)

  min = int(m.group(1))
  max = int(m.group(2))
  c = m.group(3)
  p = m.group(4)

  p = re.sub(r"[^{}]+".format(c), '', p)
  l = len(p)

  return l >= min and l <= max


def is_valid_2(entry):
  m = re.search('(\d+)-(\d+) (.): (.*)', entry)

  x = int(m.group(1)) - 1
  y = int(m.group(2)) - 1
  c = m.group(3)
  p = m.group(4)

  # XOR
  return (p[x] == c) != (p[y] == c) 

'''
Solution 1

'''

v = 0
for p in data:
  if is_valid(p): v += 1

print('Solution 1:', v)


'''
Solution 2

'''

v = 0
for p in data:
  if is_valid_2(p): v += 1

print('Solution 2:', v)