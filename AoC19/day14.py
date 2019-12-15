import sys
from math import ceil


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

data = dict()
dictint = lambda x: (x[1], int(x[0]))
pairs = lambda s: dict(dictint(x.split(' ')) for x in s.split(', '))
data = [pairs(x) for l in open(f) for x in l.strip().split(' => ')]

l, r = [], []
for i in range(0, len(data), 2):
  '''
  r-list: derived element AB
  l-list: element(s) used to make A, B => AB

  both l-list + r-list can be zipped in a loop.
  '''
  l.append(data[i])
  r.append(data[i+1])

# for a, b in zip(l, r): print(a, '==>', b)


def qty(element: str):
  '''
  element: A
  '''
  if element == 'FUEL': return 1

  q = 0
  for i, recipe in enumerate(l):
    '''
    + Find any stuff our element was used to cook and qty used
    '''
    if element in recipe:
      '''
      found: 3 A, 4 B => 1 AB

      it was used to cook AB (lethal stuff)
      '''
      parent, *_ = list(r[i])
      parent_batch_qty = r[i][parent]

      '''
      Find out how many 'AB's have been used 
      to make something else recusively.
      '''
      q += ceil(qty(parent) / parent_batch_qty) * recipe[element]

  return q

print(qty('ORE'), 'ORE', '==> 1 FUEL')
