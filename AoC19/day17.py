import sys
from collections import OrderedDict
from math import ceil
from lib.intcode import Machine
from time import sleep
import subprocess


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]

class Bot:
  SCAFFOLD = 35
  SPACE = 46
  CORNER = 64
  NORTH = 94
  SOUTH = 118
  WEST = 60
  EAST = 62
  LN = 10
  TILES = {
    35: '⬜',
    46: '.',
    2: '⭐'
  }

  def __init__(self, m):
    self.__m = m
    self.__cpu = Machine(self.__m[:])
    self.__history = []
    
    self.__bounds = (0, 0, 0, 0)
    self.__pos = (0, 0)
    self.__bot_pos = (0, 0, ord('^'))
    self.__moves = []
    self.__map = OrderedDict()
    self.__star_dust = 0

    if verbose: self.__cpu.toggle_verbose()


  def run(self, display = True):

    moves = self.traverse()
    
    m = self.__m[:]
    m[0] = 2
    cpu = self.__cpu = Machine(m)
    subs = self.subroutines(moves)

    if verbose: cpu.toggle_verbose()

    ''' 1. MAIN '''
    for instr in map(ord, subs[0]):
      cpu.run(instr)

    cpu.run(10) # return
    self.video(display)


    ''' 2. SUBROUTINES '''
    for i in range(3):
      key = (65, 66, 67)[i]

      for instr in map(ord, subs[key]):
        cpu.run(instr)
          
        self.video(display)

      cpu.run(10) # return
      self.video(display)


    ''' 3. VIDEO FEED: YES '''
    cpu.run(ord('y' if display else 'n'))
    cpu.run(10) # return
    self.video(display)

    return self.video(display)


  def ready(self):
    return self.__cpu.halted()

  def subroutines(self, moves):
    routines = {}

    A, B, C = 65, 66, 67

    '''
    Not proud of solving manually 
    but this is DAY THREE 😳

    '''
    FUNC_MAIN = 'A,A,B,B,C,B,C,B,C,A'

    FUNC_A = 'L,10,L,10,R,6'
    FUNC_B = 'R,12,L,12,L,12'
    FUNC_C = 'L,6,L,10,R,12,R,12'

    
    routines[0] = FUNC_MAIN
    routines[A] = FUNC_A
    routines[B] = FUNC_B
    routines[C] = FUNC_C

    return routines

  
  def map(self, display = True):
    cpu = self.__cpu

    cpu.run()

    return self.video(display)

  
  def get_map(self):
    return self.__map

  
  def video(self, show = True):
    cpu = self.__cpu
    pos = self.__pos = (0, 0)
    rpos = None

    while cpu.has_output():
      
      o = cpu.output()


      if o == self.LN:
        x, y = pos

        if x == 0:
          pos = (x, 0)

        else:
          pos = (0, y+1)
      
        self.update_bounds(pos)

      elif o > 127:
        self.__star_dust = o
        break

      else:
        '''capture robot position and direction'''
        if o in {self.NORTH, self.SOUTH, self.WEST, self.EAST}:
          rpos = self.__bot_pos = (*pos, o)
          
        x, y = pos
        pos = (x+1, y)
        self.__map[pos] = o

        self.update_bounds(pos)

    pos = (0, 0)   
    self.update_bounds(pos)

    if show: 
      display(self.__map, self.get_bounds(), 0, 0)

    return self.__map, rpos


  def traverse(self):
    m = self.__map

    prev = None

    *pos, facing = self.__bot_pos

    pos = tuple(pos)
    d, facing = self.turn(facing, pos, None)

    moves = []


    while True:

      s, pos, prev = self.steps(pos, facing)

      if s == 0:
        print('DEBUG', s, pos, chr(m[pos]), prev, d)
        break

      moves.append(d) 
      moves.append(s) 
      

      if pos not in m:
        # print('DEBUG POS 404', pos, d, chr(facing))

        return moves
        
      if m[pos] != self.CORNER:
        # print('DEBUG HALT NOT A CORNER', pos)
        break

      d, facing = self.turn(facing, pos, prev)
      
    self.__moves = moves
    self.__bot_pos = (*pos, facing)


    return moves


  def steps(self, pos, facing):
    m, steps, prev = self.__map, 0, None

    steps += 1
    prev = tuple(pos)
    pos = self.move(pos, facing)
    
    while pos in m and m[pos] != self.CORNER:
      steps += 1
      prev = tuple(pos)
      pos = self.move(pos, facing)

    return steps, pos, prev


  def turn(self, facing, pos, prev):
    '''
    turn() is doing 2 things:

    1. figure out which side the neighbouring scaffold node is on
    2. determine where robot is facing after turn

    '''
    n = neighbours(self.__map, pos, lambda np, v: v == Bot.SCAFFOLD and np != prev)[0]

    if n[0] != pos[0]: # W < -- > E

      return (ord('L'), ord('<')) if n[0] < pos[0] else (ord('R'), ord('>'))

    else: # N < -- > S
      return (ord('L'), ord('^')) if n[1] < pos[1] else (ord('R'), ord('v'))


  def move(self, pos, facing):

    dnswe = {
      self.NORTH: (0, -1), 
      self.SOUTH: (0, 1), 
      self.WEST: (-1, 0), 
      self.EAST: (1, 0)
    }

    return tuple(a + b for a, b in zip(pos, dnswe[facing]))


  def get_bounds(self):
    return self.__bounds


  def update_bounds(self, xy):
    mxy = list(self.__bounds)

    self.__bounds = tuple([min(p1, p2) for p1, p2 in zip(mxy[:2], xy)] + [max(p1, p2) for p1, p2 in zip(mxy[2:], xy)])


  def get_stardust_count(self):
    return self.__star_dust




def display(m, bounds, inter, corners):
  minx, miny, maxx, maxy = bounds
  maxx, maxy = abs(minx) + maxx, abs(miny) + maxy

  dash = 'INT: {}, CNR: {}, Max (x): {}, Max (y): {}'.format(inter, corners, maxx, maxy)

  subprocess.call("clear")

  print(dash)
  print('.'*(maxx+1))

  grid = [[' ']*(maxx+1) for _ in range(maxy+1)]

  for (x, y), v in m.items():
    x += abs(minx)
    y += abs(miny)

    if x < 0 or x > maxx or y < 0 or y > maxy: break

    try:
      grid[y][x] = chr(v)
    except Exception as err:
      print("Unexpected error:", err)
      print('DEBUG', x, y, maxx, maxy)
      exit()
      break

  for l in grid: print(''.join(l))

  print('\n')
  print('.'*(maxx+1))
  print(dash)

  # sleep(0.1)


def neighbours(m: dict, pos: tuple, l: callable = lambda p, v: True):
  '''
  N (x, y), S (x, y), W (x, y), E (x, y)
  '''
  (x, y), dxy = pos, [(0, -1), (0, 1), (-1, 0), (1, 0)]

  n = [(x + dx, y + dy) for dx, dy in dxy]

  return [nn for nn in n if nn in m and l(nn, m.get(nn)) ]


def corner(p, nodes):
  xcount = len([n for n in nodes if p[0] == n[0]])
  ycount = len([n for n in nodes if p[1] == n[1]])

  return xcount > 0 and ycount > 0



robo = Bot(mreset[:])
m, rpos = robo.map(False)

def one(r):
  '''
  Solution 1

  '''
  m = r.get_map()

  acc, inter, corners = 0, 0, []
  for (x, y), v in m.items():
    if v != Bot.SCAFFOLD: 
      continue

    n = neighbours(m, (x, y), lambda np, v: v == Bot.SCAFFOLD)

    if len(n) == 4:
      acc += (x-1) * y
      m[(x, y)] = 79
      inter += 1

    elif len(n) == 2 and corner((x,y), n):
      # m[(x, y)] = 64
      corners.append((x, y))



  display(m, r.get_bounds(), inter, len(corners))

  print('Solution 1 \n--------------------------------------------------')
  print('SUM OF ALIGNMENT PARAMS:', acc)

  
def two(r):
  '''
  Solution 2

  '''
  print('Solution 2 \n--------------------------------------------------')

  r.run(False)
  
  print('STARDUST COUNT:', r.get_stardust_count())


'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two(robo)
else: 
  one(robo)



'''
AN ODE TO MY STRUGGLES
--------------------------------------------------------------------

[12, 'R', 12, 'L', 12, 'L'] 

[
  A, 3, B, 3, 1, A, B, 3, 1, B, 3, 1, B, A, 3, 3, B, 3, 3, B, 3, 3, B, 3, 3, B, 3, 3, A, 3, 3, A, B, 3, 1, A, 3, 3, A, 3, 3, B, 3, 3, A, 3, 3, A, 3, 3, B, B, 3, 1, B, 3, 3, A, 3, 3, A, 3, 3, A, 3, 3, B, 3, 3, B, A, 3, 1, B, 3, 3, B, 3, 3, B, 3, 1, A, 3, 1, B, 1
]

65 : L, 9, R, 9, 1, L, 6, R, 9, 1, R, 9, 1, R, 6, L, 9, 3, R, 9, 3, R, 9, 3, R, 9, 3, R, 9, 3, L
66 : 9, 3, L, 6, R, 9, 1, L, 9, 3, L, 9, 3, R, 9, 3, L, 9, 3, L, 9, 3, R, 6, R, 9, 1, R, 9, 3, L
67 : 9, 3, L, 9, 3, L, 9, 3, R, 9, 3, R, 6, L, 9, 1, R, 9, 3, R, 9, 3, R, 9, 1, L, 9, 1, R, 7

[9, 3, R, 9, 3]

|66|

L 9 
R 10 

L 6 

R 10 R 10 R 6 L 12 R 12 R 12 R 12 R 12

L 12 L 6 R 10 L 12 L 12 R 12 L 12 L 12 R 6 R 10 R 12 

L 12 L 12 L 12 R 12 R 6 L 10 R 12 R 12 R 10 L 10 R 7

|20|

R 10 R 10 R 6 R 12 R 12 R 10 R 6 R 12 R 12 R 12

|48|L 9 R 10 L 6 R 10 R 10 R 6 L R R R R L L 6 R 10 L L R L L R 6 R 10 R L L L R R 6 L 10 R R R 10 L 10 R 7

|40|L 9 R L 6 R R R 6 L R R R R L L 6 R L L R L L R 6 R R L L L R R 6 L R R R L R 7

|66|L 9 R ___B___ L 6 R ___B___ R ___B___ R 6 L ___A___ R ___A___ R ___A___ R ___A___ R ___A___ L ___A___ L 6 R ___B___ L ___A___ L ___A___ R ___A___ L ___A___ L ___A___ R 6 R ___B___ R ___A___ L ___A___ L ___A___ L ___A___ R ___A___ R 6 L ___B___ R ___A___ R ___A___ R ___B___ L ___B___ R 7


|375|L111111111R1111111111L111111R1111111111R1111111111R111111L111111111111R111111111111R111111111111R111111111111R111111111111L111111111111L111111R1111111111L111111111111L111111111111R111111111111L111111111111L111111111111R111111R1111111111R111111111111L111111111111L111111111111L111111111111R111111111111R111111L1111111111R111111111111R111111111111R1111111111L1111111111R1111111

R,L,L,R,L,L

L,10,L
10,R,6
R,12,L,12,L

'''