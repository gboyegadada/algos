import sys

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

data = []
for l in open(f):
  data.append(l.strip())

def step(d, mx, my, xl, yl, x=0, y=0, c=0):
  x = (x + mx) % xl
  y = y + my

  if '#' == d[y][x]: c += 1

  return c if y == yl-1 else step(d, mx, my, xl, yl, x, y, c)


'''
Solution 1

'''

ans = step(data, 3, 1, len(data[0]), len(data))

print('Solution 1:', ans)


'''
Solution 2

'''

slopes = [
  (1, 1),
  (3, 1),
  (5, 1),
  (7, 1),
  (1, 2)
]

ans = 1
for mx, my in slopes:
 ans *= step(data, mx, my, len(data[0]), len(data))

print('Solution 2:', ans)