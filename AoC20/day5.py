import sys
import math

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]


def get_row_id(s: str):
  ab = (0, 127)
  for a in s[:7]:
    t = math.ceil((ab[1]-ab[0])/2)
    ab = (ab[0], ab[1] - t) if 'F' == a else (ab[1]-t+1, ab[1])

  return ab[0]

def get_col_id(s: str):
  ab = (0, 7)
  for a in s[7:]:
    t = math.ceil((ab[1]-ab[0])/2)
    ab = (ab[0], ab[1] - t) if 'L' == a else (ab[1]-t+1, ab[1])

  return ab[0]

def get_id(s: str):
  r = get_row_id(s)
  c = get_col_id(s)

  return (r * 8) + c



h = 0
prev = None
manifest = []

for l in open(f):
  s = l.strip()

  id = get_id(s)
  manifest.append(id)

manifest = sorted(manifest)


'''
Solution 1

'''
print('Solution 1:', max(manifest))



'''
Solution 2

'''
for id in manifest:
  if id+1 not in manifest and id+2 in manifest:
    print('Solution 2:', id+1)
    break