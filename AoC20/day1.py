import sys

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

data = []
for l in open(f):
  data.append(int(l.strip()))

def pair(n, d):
  r = None
  for x in d:
    y = n - x

    if y in d:
      r = (x, y)
      break

  return r


'''
Solution 1

'''

ans = pair(2020, data)

if ans != None:
  print('Solution 1: ', ans[0] * ans[1])



'''
Solution 2

'''

s = None
for x in data:
  yz = 2020 - x
  a = pair(yz, data)

  if a != None:
    s = (x,) + a
    break

if s != None:
  print('Solution 2:', s[0] * s[1] * s[2])