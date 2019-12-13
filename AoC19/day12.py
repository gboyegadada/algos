import sys
import itertools
from functools import reduce
from math import gcd

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
    spos = 'pos=<x={0}, y={1}, z={2}>'.format(*self.pos)
    svel = 'vel=<x={0}, y={1}, z={2}>'.format(*self.vel)

    return '{0}, {1}'.format(spos, svel) 

moons = []
for l in open(f):
  pos = [int(x[2:]) for x in l.strip('<>\n').split(', ')]
  vel = [0, 0, 0]
  moons.append(Body(pos, vel))

def lcm(a, b):
  return (a * b) // gcd(a, b)

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


'''
Solution 1

'''

def one(moons):
  print('Solution 1:', '\n------------------------------------\n')
  print('Input steps:')
  steps=int(sys.stdin.readline())

  print('\nAfter', 0, 'steps:')
  for m in moons:
    print(m)
    
  for i in range(steps):
    step(moons)
    
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

LCM works because each axis is cycling independently. Let's do a simple example:

3 series, each repeating at a different period. If the state is based on all 3 series, 
then how long until we see the same state again?

    0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
S1: 0 1 2 3 0 1 2 3 0 1 2 3 0 1 2 3 0
S2: 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
S3; 0 1 2 3 4 5 0 1 2 3 4 5 0 1 2 3 4
S1 has a period of 4, S2 of 2, S3 of 6. And the combined series has a period of 12, 
which is the LCM of 2, 4, and 6. You'll get pairwise repetitions earlier than that.

S1 and S2 have a combined period of 4. S2 and S3 have a combined period of 6. 
But S1 and S3 have a combined period of 12.

There's a more mathematically rigorous way to describe this, but the 
above illustrates what's happening.

Explanation by u/rabuf (https://www.reddit.com/user/rabuf/) 
'''

def two(moons):
  print('Solution 2:', '\n------------------------------------\n')

  '''
  This will be our clock. Tracking the time (or steps or ticks) it has taken for a moon 
  to reach it's current position in orbit.
  '''
  steps = 0
  
  '''
  We will capture the orbital periods (https://en.wikipedia.org/wiki/Orbital_period) for each axis here:
  {
    0: step at which all 4 moons are at their starting x-position and x-velocity
    1: step at which all 4 moons are at their starting y-position and y-velocity
    2: step at which all 4 moons are at their starting z-position and z-velocity
  }
  '''
  period =  dict()

  '''
  Save starting values grouped by axis:
  0: (position_x, velocity_x) * (4 moons)
  1: (position_y, velocity_y) * (4 moons)
  2: (position_z, velocity_z) * (4 moons)
  '''
  start = [[(m.pos[axis], m.vel[axis]) for m in moons] for axis in range(3)]

  while len(period) < 3:
    steps += 1
    step(moons)

    for axis in range(3):
      '''
      See if current (pos_axis, vel_axis) for all moons match their starting values:
      '''
      if axis not in period and start[axis] == [(m.pos[axis], m.vel[axis]) for m in moons]: 
        period[axis] = steps

  print('After', steps, 'steps:')
  print('ans:', reduce(lcm, period.values()))


'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two(moons)
else: 
  one(moons)
