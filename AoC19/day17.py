import sys
from collections import OrderedDict
from math import ceil
from itertools import combinations
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
    self.__alignment_parameters = 0
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
      key = ('A', 'B', 'C')[i]

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

    '''
    Initially solved manually not proud 
    but this was DAY THREE 😳

    FUNC_MAIN = 'A,A,B,B,C,B,C,B,C,A'

    FUNC_A = 'L,10,L,10,R,6'
    FUNC_B = 'R,12,L,12,L,12'
    FUNC_C = 'L,6,L,10,R,12,R,12'

    
    routines[0] = FUNC_MAIN
    routines[A] = FUNC_A
    routines[B] = FUNC_B
    routines[C] = FUNC_C
    


    UPDATE: DAY AFTER
    ------------------------------------------
    build list of candidate functions (collect repeated sequences)

    1. begin from [i:i+2] 
    2. count occurences of sub in rest of string
    3. if zero, increment i
    4. if repetitions found, store count, increment j and try [i:j] until j >= j + (len(moves) - j) // 2
    5. increment i and goto step 1

    '''
    path, n, seen = ','.join(moves), '', set()

    counts, l, i, j = {}, len(moves), 0, 2

    while i < l:
      n = ','.join(moves[i:j])
      
      if n not in seen:
        seen.add(n)
        c = ','.join(moves[j:]).count(n)

        if c > 1:
          counts[n] = c
      
      if j >= j + (l-j)//2 or c == 0:
        i += 1
        j = i + 2
      else:
        j += 1


    print('PATH:', path, '\n')

    # for p, c in counts.items():
    #   print('PATH:', p, '==>', c)

    '''
    do a little checksum using combinations of candidate functions
    to narrow down list and group candidate functions into trios. 

    '''
    h = path.replace(',', '') # for checksum
    found = set()
    total_count = 0
    for _abc in combinations(counts.keys(), 3):
      total_count += 1
      a, b, c = map(lambda s: s.replace(',', ''), _abc)

      '''
      check if total length of the overall path matches 
      combined steps of candidate functions (minus commas).
      '''
      checksum = (h.count(a) * len(a)) + h.count(b) * len(b) + h.count(c) * len(c)
      if len(h) == checksum:
        found.add(_abc)
        
    print(f'ABC CANDIDATES: {len(found)} found out of {total_count} combinations.')


    '''
    simulate traversal with each set of functions and stop when we
    find a function trio that takes us all the way to the end of the maze.
    '''
    abc, fn_queue, queue = {}, [], ''
    while found and queue != path:
      func_set = found.pop()
      abc, queue, fn_queue = dict(zip('ABC', func_set)), '', []

      while queue != path:
        match = False
        for i, fn in enumerate(func_set):
          new_queque = f'{queue},{fn}' if queue != '' else fn
          
          if path.startswith(new_queque):
            queue = new_queque
            fn_queue.append('ABC'[i])
            match = True
            break

        if not match: 
          break

    print('ABC DEFS:', abc, fn_queue)


    '''
    DONE !!

    return subroutines
    '''
    routines[0] = ','.join(fn_queue)
    for k, f in abc.items():
      routines[k] = f


    return routines

  
  def map(self, display = True):
    cpu = self.__cpu

    cpu.run()

    self.video(display)
    
    m, acc, inter, corners = self.__map, 0, 0, []
    for (x, y), v in m.items():
      if v != Bot.SCAFFOLD: 
        continue

      n = neighbours(m, (x, y), lambda np, v: v == Bot.SCAFFOLD)

      if len(n) == 4:
        acc += (x-1) * y
        m[(x, y)] = 79
        inter += 1

      elif len(n) == 2 and corner((x,y), n):
        m[(x, y)] = 64
        corners.append((x, y))

    self.__alignment_parameters = acc

    return self.__map, self.__bot_pos
  

  def get_map(self):
    return self.__map

  
  def video(self, show = True):
    cpu = self.__cpu
    pos = self.__pos = (0, 0)

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
          if self.__bot_pos[0] == 0: 
            self.__bot_pos = (*pos, o)
          
        x, y = pos
        pos = (x+1, y)
        self.__map[pos] = o

        self.update_bounds(pos)

    pos = (0, 0)   
    self.update_bounds(pos)

    if show: 
      display(self.__map, self.get_bounds(), 0, 0)

    return self.__map, self.__bot_pos


  def traverse(self):
    m = self.__map.copy()

    prev = None

    x, y, facing = self.__bot_pos

    pos = tuple([x+1, y])
    d, facing = self.turn(facing, pos, None)


    moves = []


    while True:

      s, pos, prev = self.steps(pos, facing)
      # print('DEBUG', s, pos, chr(m[pos]), prev, chr(d), chr(facing))

      if s == 0:
        break

      moves.append('{},{}'.format(chr(d), s)) 
      

      if pos not in m or m.get(pos, None) != self.CORNER:
        print('DEBUG HALT NOT A CORNER', pos, s)
        break

      d, facing = self.turn(facing, pos, prev)
      
    self.__moves = moves
    self.__bot_pos = (*pos, facing)



    return moves


  def steps(self, pos, facing):
    m, steps, prev = self.__map, 0, None

    p = tuple(pos)
    p = self.move(p, facing)
    
    while p in m and m.get(p) not in {self.CORNER, self.SPACE}:
      steps += 1
      prev = tuple(pos)
      pos = p

      p = self.move(p, facing)

    if m.get(p, None) == self.CORNER:
      steps += 1
      prev = tuple(pos)
      pos = p


    return steps, pos, prev


  def turn(self, facing, pos, prev):
    '''
    turn() is doing 2 things:

    1. figure out which side the neighbouring scaffold node is on
    2. determine where robot is facing after turn

    '''
    n = neighbours(self.__map, pos, lambda np, v: v == Bot.SCAFFOLD and np != prev)[0]


    if n[0] != pos[0]: # N < -- > S
      f = ord('<') if n[0] < pos[0] else ord('>')

    else: # W < -- > E
      f = ord('^') if n[1] < pos[1] else ord('v')

    if '{} {}'.format(chr(facing), chr(f)) in {'^ <', '< v', 'v >', '> ^'}:
      return (ord('L'), f)
    elif '{} {}'.format(chr(facing), chr(f)) in {'^ >', '> v', 'v <', '< ^'}:
      return (ord('R'), f)


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


  def get_alignment_parameters(self):
    return self.__alignment_parameters




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
  # m = r.get_map()
  # display(m, r.get_bounds(), inter, len(corners))

  print('Solution 1 \n--------------------------------------------------')
  print('SUM OF ALIGNMENT PARAMS:', r.get_alignment_parameters())

  
def two(r):
  '''
  Solution 2

  '''
  print('Solution 2 \n--------------------------------------------------')

  r.run(False)
  
  print('\n', 'STARDUST COUNT:', r.get_stardust_count(), sep='')


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