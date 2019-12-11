import sys
import math
from itertools import groupby 

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
def dist(a, b, scale = 1):
  x1, y1, x2, y2 = a[0]*scale, a[1]*scale, b[0]*scale, b[1]*scale
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

'''
Returns radian for (x, y) as sort key
'''
radkey = lambda x: math.atan2(x[0], x[1])

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
  dst = math.sqrt(dx**2 + dy**2)
  rad = math.atan2(dx, dy)

  return (x2, y2, rad, dst)


'''
Solution 1

'''
xf, yf, d, b = 0, 0, None, None

for x, y in coords:
  s = {(rad) for x, y, rad, dst in (line(x, y, px, py) for px, py in coords if (px,py) != (x,y))}
  _d = len(s)

  if d == None or _d > d: 
    d, b, ai = _d, [x, y], x+(y*nx)


print('Solution 1\n')
for i in range(0, len(m), nx):
  print(str(i//nx).zfill(2), '|  ', '   '.join('😜' if ai == i+j else x for j, x in enumerate(list(m[i:i+nx]))).replace('#', '+'))
  print(' ')

print('BASE:', b)
print('ASTEROIDS:', d, '\n')


'''
Solution 2

'''
print('Solution 2\n')

x, y = b

s = [line(x, y, px, py) for px, py in coords]
s.sort(key=lambda x: x[2], reverse=True)
rsteps = list({(rad) for px, py, rad, dst in s})

rsteps.sort(reverse=True)

mp = []
for j, i in groupby(s, lambda a: a[2]): 
  l = list(i)
  l.sort(key=lambda x: x[3], reverse=True)
  mp.append(l)

start = math.radians(90)
start_index = 0
print('STARTING FROM', start, 'RAD')
for i, x in enumerate(mp):
  if x[0][2] >= start:
    start_index = i
    # print('FOUND', x)
    break
print('----------------------\n')

mp = mp[start_index:] + mp[0:start_index]
current, count, i = None, 0, 0
ans = None
while count < 200: 
  if len(mp[i]) > 0: 
    current = mp[i].pop()
    # print('STEP ', math.degrees(current[2]))
    if current[0] == b[0] and current[1] == b[1]: continue
    count += 1
    if count == 200: ans = current

  i += 1
  if i == len(mp): i = 0

print('ANS', ans, (ans[0]*100) + ans[1])