import sys


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  data = [int(x) for x in l.strip()]


def solve_digit(pos: int, digits: list):
  dl = len(digits)

  base_seq = [0]*(pos+1) + [1]*(pos+1) + [0]*(pos+1) + [-1]*(pos+1)
  seq = base_seq[1:] + base_seq * ((dl // len(base_seq)) + 1)


  acc = 0

  for d, s in zip(digits, seq[:dl]): 
    acc += d * s

  return abs(acc) % 10


for _ in range(100):
  data = [ solve_digit(i, data) for i in range(len(data)) ]

print('Solution 1:', ''.join(map(str, data[:8])))



