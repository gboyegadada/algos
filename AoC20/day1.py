import sys

if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

data = []
for l in open(f):
  data.append(int(l.strip()))

for x in data:
  y = 2020 - x

  if y in data:
    print('Answer is:', x * y)
    break

