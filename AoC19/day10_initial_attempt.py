import sys
import math
from functools import lru_cache


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

m, nx, ny = '', 0, 0

for l in open(f): 
  m += l.strip()

  ny += 1
  if nx == 0: nx = len(l)-1


'''
Assuming you know the coordinates of all the points and obstacles (and holes?), 
you can follow the below steps.
------------------------------------------------------------------------

Points P1(x1,y1) and P2(x2,y2). 
Let obstacle be O(x3,y3).

Check the distance between P1 and P2. Compare it with that of P1->O + O->P2. 

if both are the same, them O lies between P1 and P2 and is in LoS.

Euclidean distance between two points -> sqrt((x2-x1)^2+(y2-y1)^2))

'''

def mem(f):
  m = {}

  def helper(a, b):
    k = '{0}.{1}.{2}.{3}'.format(a[0], a[1], b[0], b[1])
    if k not in m: m[k] = f(a, b)
    return m[k]

  return helper

 
'''
+ Euclidean distance between two points -> sqrt((x2-x1)^2+(y2-y1)^2))
'''
@mem
def dist(a, b, scale = 2000):
  x1, y1, x2, y2 = a[0]*scale, a[1]*scale, b[0]*scale, b[1]*scale
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

'''
+ Check the distance between a and b. Compare it with that of a->O + O->b.
+ If both are the same, them O lies between a and b and is in LoS.
'''
def los(a, b, d):
  for x in d:
    if dist(a, b) == (dist(a, d[x]) + dist(b, d[x])):
      return False

  return True


def sweep(x, y, r, detected):
  xi = x - r
  yi = y - r

  _detected = {}
  _skipped = {}

  xdip, ydip, movx = False, False, False
  for _ in range(r * 2 * 4):
    if yi >= 0 and yi < ny and xi >= 0 and xi < nx and m[yi*nx + xi] == '#': 
      if los([x,y], [xi,yi], {**detected, **_detected, **_skipped}) == True:
        _detected['{0}.{1}'.format(xi,yi)] = [xi,yi]
        # print('Detected... [ x: {0}, y: {1} ]'.format(xi, yi))
      else:
        _skipped['{0}.{1}'.format(xi,yi)] = [xi,yi]

    if not movx: 
      yi += -1 if ydip else 1
    else: 
      xi += -1 if xdip else 1

    if movx and (xi == x + r or xi == x - r):  
      xdip = not xdip
      if movx: movx = False
    
    elif not movx and (yi == y + r or yi == y - r): 
      ydip = not ydip
      if not movx: movx = True

  return (_detected, _skipped)

def search(x, y):
  detected = {}
  skipped = {}

  for r in range(1, nx):
    d, s = sweep(x, y, r, {**detected, **skipped})
    detected = {**detected, **d}
    skipped = {**skipped, **s}

  return detected


xf, yf, d, b = 0, 0, None, None

for p in range(ny*nx):
  if m[p] == '.': continue

  x, y = p % nx, p // nx
  _d = search(x, y)

  if d == None or len(_d) > len(d): 
    d, b = _d, [x, y]

print('BASE:', b)
print('ASTEROIDS:', len(d), '\n')

for i in range(0, len(m), nx):
  print(str(i//nx).zfill(2), '|  ', '   '.join(list(m[i:i+nx])).replace('#', '+'))
  print(' ')

