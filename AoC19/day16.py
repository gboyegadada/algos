import sys
from math import ceil
from itertools import accumulate


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  data = [int(x) for x in l.strip()]


def num(l):
  return sum([ x * 10**i for i, x in enumerate(reversed(l))])

def solve_digit(pos: int, digits: list):
  
  base_seq = [0]*(pos+1) + [1]*(pos+1) + [0]*(pos+1) + [-1]*(pos+1)  
  seq = base_seq[pos+1:] + base_seq * ceil(len(digits) // len(base_seq))


  # st = []
  acc = 0

  for d, s in zip(digits[pos:], seq[:len(digits)-pos]): 
    # st.append('{}*{}'.format(d, s))
    acc += d * s

  # print(' + '.join(st), '=', abs(acc) % 10, '\n')
  return abs(acc) % 10


'''
Solution 1

'''

d = data[:]

for _ in range(100):
  d = [ solve_digit(i, d) for i in range(len(d)) ]

print('Solution 1:', num(d[:8]))


'''
Solution 2


1st digit -------> no zeros 
2nd digit -------> 1 zeros | 0  1  1  0  0 -1 -1  0  0 ...
3rd digit -------> 2 zeros | 0  0  1  |  1  1  0  0  0 -1 -1 -1 ...
4th digit -------> 3 zeros | 0  0  0  1 | 1  1 ... 
5th digit -------> 4 zeros | 0  0  0  0  1 | 1 1 1 1 0 0 0 0 0 -1 -1 -1 -1 -1 ...

(3M + 1)th ------> 3M zeros

......................................................................

1. By the time we get to index [5976463] all sums before that point will be ZEROs 
   so we will ignore them.

2. On the other half of our sequence, coeficients are all ones.
   
        0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1
        <------<-------|------>------->

3. Calculate in reverse and reverse our answer again.

'''
skip = num(data[:7])
d = (data * 10000)[skip:][::-1]

for _ in range(100):
  d = accumulate(d, lambda a, b: abs(a + b) % 10)

print('Solution 2:', num(list(d)[::-1][:8]))
