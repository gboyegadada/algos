import sys
from collections import OrderedDict
from lib.intcode import Machine
from lib.helper import display
from time import sleep
import subprocess


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]

class Drone:

  def __init__(self, m):
    self.__m = m
    self.__cpu = Machine(self.__m[:])
    self.__history = []
    
    self.__bounds = (0, 0, 0, 0)
    self.__pos = (0, 0)
    self.__map = OrderedDict({(0, 0): 1})

    if verbose: self.__cpu.toggle_verbose()



  def points(self, silent = False, bounds = 0):
    p = self.__pos = (0, 0)

    points = 0
    ship_pos = None

    for y in range(bounds):
      for x in range(bounds):
        p = self.__pos = (x, y)

        o = self.ping(x, y)
        self.__map[p] = '#' if o == 1 else '.'
        self.update_bounds(p)
        points += o

    if not silent: 
      display(self.__map, self.__bounds)

    return points, ship_pos


  def position(self, bounds = 0):
    x, y = 0, 0

    while True:
      
      lower_left = None

      while True:
        '''
        find lower left corner first
        '''

        lower_left = self.ping(x, y)

        if lower_left == 1: break
        
        x += 1


      b = bounds - 1 # make corners inclusive

      ''' lower right corner '''
      x2 = x + b
      lower_right = self.ping(x2, y)
      
      ''' upper left corner '''
      upper_left = self.ping(x, y-b)

      ''' upper right corner '''
      upper_right = self.ping(x2, y-b)

      ''' 
      test:

      check that the spot just above the top right corner is
      not a (#).

      making the sure the box fits right on the edge.
      '''
      upper_right_test = self.ping(x2, y-bounds)

      if upper_left and lower_left and lower_right and upper_right and not upper_right_test:
        return (x, y-b)

      y += 1

    ''' FAILED '''
    return (0, 0)


  def ping(self, x, y):
    cpu = self.__cpu
  
    cpu.boot()

    cpu.run(x)
    cpu.run(y)

    return cpu.output()


  def update_bounds(self, xy):
    mxy = list(self.__bounds)

    self.__bounds = tuple([min(p1, p2) for p1, p2 in zip(mxy[:2], xy)] + [max(p1, p2) for p1, p2 in zip(mxy[2:], xy)])

      


def one(d):
  '''
  Solution 1

  '''

  print('Solution 1 \n--------------------------------------------------')
  robo = Drone(d)
  points, _ = robo.points(bounds=50)

  print('========================================')
  print('POINTS:', points)

  
def two(d):
  '''
  Solution 2

  '''
  print('Solution 2 \n--------------------------------------------------')
  robo = Drone(d)
  x, y = robo.position(bounds=100)

  print('========================================')
  print(f'Ship should fit at (x: {x}, y: {y})')
  print(f'ANS: {(x * 10000) + y}')


'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two(mreset[:])
else: 
  one(mreset[:])
