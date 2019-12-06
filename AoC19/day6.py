
import sys

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

with open(f, 'r') as fp:

  l, r = fp.readline(), []
  while l:
    r += [str(l).strip()]
    
    l = fp.readline()

  
pl, pr = [s[:s.index(')')] for s in r], [s[s.index(')')+1:] for s in r]

def orbits(p, return_array = True):

  r = [pl[p]] if return_array else 1

  if pl[p] in pr:
    po = pr.index(pl[p])

    return r + orbits(po, return_array)
  else:
    return r


'''
Part 1

'''
def total():
  t = 0
  for i in range(len(pl)):
    t += orbits(i, False)

  print('TOTAL', t)


'''
Part 2

'''
def dist(a, b = 'COM'):
  ao = orbits(pr.index(a))

  if b not in {'COM', None}:
    bo = orbits(pr.index(b))

    for i in ao[:]:
      if i in bo:
        ao.remove(i)
        bo.remove(i)
  else: 
    bo = []


  print('Minimum orbits between ({0}) and ({1}):'.format(a, b), len(ao+bo))

total()
dist('YOU', 'SAN')