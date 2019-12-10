import sys
import math

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

coords =  [(i%nx, i//nx) for i, p in enumerate(m) if p == '#']

'''
If slopes of lines with any two point will be same, 
then they are co-linear:

y2 − y1      y3 − y1
-------  =  ---------
x2 − x1      x3 − x1

'''
def line(x1, y1, x2, y2):
  dx, dy =  x2 - x1, y2 - y1

  d = abs(math.gcd(dx, dy))
  dx = dx//d if d else 0
  dy = dy//d if d else 0

  return (dx, dy)



xf, yf, d, b = 0, 0, None, None

for x, y in coords:
  s = { (dx, dy) for dx, dy in (line(x, y, px, py) for px, py in coords) }
  _d = len(s)-1

  if d == None or _d > d: 
    d, b, ai = _d, [x, y], x+(y*nx)


for i in range(0, len(m), nx):
  print(str(i//nx).zfill(2), '|  ', '   '.join('😜' if ai == i+j else x for j, x in enumerate(list(m[i:i+nx]))).replace('#', '+'))
  print(' ')

'''
Part 1

'''
print('BASE:', b)
print('ASTEROIDS:', d, '\n')

