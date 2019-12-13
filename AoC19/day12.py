import sys
import itertools

if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

class Body:
  def __init__(self, p, v):
    self.pos = p
    self.vel = v

  def __str__(self):
    return 'pos=<x={0}, y={1}, z={2}>'.format(*self.pos) + ', vel=<x={0}, y={1}, z={2}>'.format(*self.vel)

moons = []
for l in open(f):
  pos = [int(x[2:]) for x in l.strip('<>\n').split(', ')]
  vel = [0, 0, 0]
  moons.append(Body(pos, vel))

def step(bodies):
  # 1. apply gravity
  for m1, m2 in itertools.combinations(range(4), 2):

    for i in range(3):
      if bodies[m1].pos[i] > bodies[m2].pos[i]:
        bodies[m2].vel[i] += 1
        bodies[m1].vel[i] -= 1
      elif bodies[m1].pos[i] < bodies[m2].pos[i]:
        bodies[m1].vel[i] += 1
        bodies[m2].vel[i] -= 1

  # 2. apply velocity
  for b in bodies:
    for i in range(3): b.pos[i] += b.vel[i]

  return bodies


'''
Solution 1

'''

def one():
  print('Solution 1:', '\n------------------------------------\n')
  print('Input steps:')
  steps=int(sys.stdin.readline())

  global moons

  print('\nAfter', 0, 'steps:')
  for m in moons:
    print(m)
    
  for i in range(steps):
    moons = step(moons)
    
    if (i+1) % (steps // 10) == 0:
      print('\nAfter', i+1, 'steps:')
      for m in moons:
        print(m)

  print('\nEnergy after', steps, 'steps:', '\n---------------------------\n')
  total = 0
  for m in moons:
    pot, kin = sum([abs(x) for x in m.pos]), sum([abs(x) for x in m.vel])
    total += pot * kin

    print('pot:', pot, '; kin:', kin, '; total:', pot * kin)

  print('\n---------------------------\n', 'total:', total)


'''
Solution 2

'''
def two():
  print('Solution 2:', '\n------------------------------------\n')


'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two()
else: 
  one()
