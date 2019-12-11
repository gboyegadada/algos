
import sys

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

pl, pr, la, lb = [], [], 0, 0
for l in open(f):
  if la == 0: la, lb = l.index(')'), len(l)-1
  pl.append(l[:la])
  pr.append(l[la+1:lb])

def mem(f):
  m = {}

  def helper(x):
    k = pl[x]
    if k not in m: m[k] = f(x)
    return m[k]

  return helper

@mem
def orbits(p):
  if pl[p] in pr:
    po = pr.index(pl[p])

    return [pl[p]] + orbits(po)
  else:
    return [pl[p]]


'''
Part 1

'''
def total():
  t = 0
  for i in range(len(pl)):
    t += len(orbits(i))

  print('TOTAL', t)


'''
Part 2

'''
def dist(a, b = 'COM'):
  ao = orbits(pr.index(a))

  if b not in {'COM', None}:
    bo = orbits(pr.index(b))

    i, al, bl = 1, len(ao), len(bo)
    while i < al :
      if ao[-i] != bo[-i]:
        ao = ao[:-i+1]
        bo = bo[:-i+1]
        break

      i += 1
  else: 
    bo = []


  print('Minimum orbits between ({0}) and ({1}):'.format(a, b), len(ao+bo))

total()
dist('YOU', 'SAN')