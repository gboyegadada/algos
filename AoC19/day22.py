import sys
from collections import OrderedDict


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

steps = [l.strip() for l in open(f)]


def parse_op(op: str):
  if op in {'deal into new stack', 'result'}:
    return [op.replace(' ', '_')]

  i = op.rfind(' ')

  return (op[:i].replace(' ', '_'), int(op[i:]))



def one(steps):
  '''
  Solution 1

  '''    
    
  def op_deal_with_increment(incr: int, deck: list):
    l = len(deck)
    new_deck = [0] * l

    p = 0 
    while deck:
      new_deck[p] = deck.pop(0)

      if p + incr < l - 1:
        p += incr
      else:
        p = (p + incr) - l

    return new_deck


  ops = {
    'deal_with_increment': op_deal_with_increment,

    'deal_into_new_stack': lambda deck: deck[::-1],

    'cut': lambda i, deck: deck[i:] + deck[:i]
  }


  deck = [x for x in range(10007)]

  for op in steps:
    f, *args = parse_op(op)

    deck = ops[f](*args, deck)

  print('Solution 1\n..............................................')
  print(deck.index(2019))

  
def two(steps):
  '''
  Solution 2

  '''

  ops = {
    'deal_with_increment': lambda x, l, a, b: (a * x % l, b * x % l),

    'deal_into_new_stack': lambda l, a, b: (-a % l, (l - 1 - b) % l),

    'cut': lambda x, l, a, b: (a, (b - x) % l)
  }


  L = 119315717514047
  N = 101741582076661
  P = 2020 # card pos

  a, b = 1, 0
  for op in steps:
    f, *args = parse_op(op)

    a, b = ops[f](*args, L, a, b)

  r = (b * pow(1-a, L-2, L)) % L

  ans = ((P - r) * pow(a, N*(L-2), L) + r) % L

  print('Solution 2\n..............................................')
  print(ans)


'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two(steps[:])
else: 
  one(steps[:])

