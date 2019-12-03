import math
from typing import List, Any

def get_data() -> List[int]:
  with open('day3_input.txt', 'r') as fp:

    l, input, count = fp.readline(), [[], []], 0
    input[0] = str(l).split(',')
    l = fp.readline()
    input[1] = str(l).split(',')

  return input


def move(x, w: int):
  if x[0] == 'L':
    for _ in range(int(x[1:])): 
      dist[w]['x'] -= 1
      points[w] += [ ":".join([str(dist[w]['x']), str(dist[w]['y'])]) ]
  elif x[0] == 'R':
    for _ in range(int(x[1:])): 
      dist[w]['x'] += 1
      points[w] += [ ":".join([str(dist[w]['x']), str(dist[w]['y'])]) ]

  elif x[0] == 'U':
    for _ in range(int(x[1:])): 
      dist[w]['y'] += 1
      points[w] += [ ":".join([str(dist[w]['x']), str(dist[w]['y'])]) ]
  elif x[0] == 'D':
    for _ in range(int(x[1:])): 
      dist[w]['y'] -= 1
      points[w] += [ ":".join([str(dist[w]['x']), str(dist[w]['y'])]) ]


def findClosest(a: List[str]):
  c = [False]
  for i in range(len(a)):
    p = list(map(lambda x: abs(int(x)), a[i].split(':')))

    # |x1 - x2| + |y1 - y2|
    # sum(c[0], c[1]) > sum(p[0], p[1])
    if c[0] == False or sum(c) > sum(p):
      c = p[:]
      continue
  return c


def findFastest(a: List[str]):
  c = [False]
  for i in range(len(a)):
    steps = [points[0].index(a[i])+1, points[1].index(a[i])+1]

    # |x1 - x2| + |y1 - y2|
    # sum(c[0], c[1]) > sum(p[0], p[1])
    if c[0] == False or sum(c) > sum(steps):
      c = steps[:]
      continue
  return c
    

d, dist, points = get_data(), [
  {'x': 0, 'y': 0},
  {'x': 0, 'y': 0}
], [[], []]

l0, l1 = len(d[0]), len(d[1])

for i2 in range(max(l0, l1) + 1):
  if (i2 < l0): move(d[0][i2], 0)
    
  if (i2 < l1): move(d[1][i2], 1)


inter = list(set(points[0]) & set(points[1]))
closest = findClosest(inter)
fastest = findFastest(inter)

print('INTER:', inter)

print('CLOSEST:', closest, sum(closest))
print('FASTEST:', fastest, sum(fastest))