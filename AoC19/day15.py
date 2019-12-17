import sys
from collections import OrderedDict
from lib.intcode import Machine
from lib.helper import shortest_path
from time import sleep
from random import randint
import subprocess


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]

class Droid:
  WALL_HIT = 0
  OK = 1
  OXYGEN_TANK_FOUND = 2
  UNEXPLORED = 3

  MOV_NORTH = 1
  MOV_SOUTH = 2
  MOV_WEST = 3
  MOV_EAST = 4

  def __init__(self, m):
    self.__m = m
    self.__cpu = Machine(self.__m[:])
    self.__history = []
    
    self.__bounds = (0, 0, 0, 0)
    self.__pos = (0, 0)
    self.__map = OrderedDict()
    self.__tiles = {
      0: '⬜',
      1: '.',
      2: '⭐'
    }

    if verbose: self.__cpu.toggle_verbose()


  def map(self, display = True):
    self.reset()

    cpu = self.__cpu
    history = self.__history
    p = self.__pos = (0, 0)
    nswe = set(range(1,5))
    move = self.MOV_NORTH
    tries = {p: {self.reverse(self.MOV_NORTH)}}


    while True:
      '''
      here, we will use (D)epth (F)irst (S)earch algo to traverse
      the entire map. Then use BFS to find shortest path.

      the goal here is to traverse every single path (even after the tank is found) by 
      going all the way to end of each path and backtracking till we find a new one.

      Loop:
      ------------------------------------------------------------------
      - each position is a new node/vertex
      - each vertex potentially has 4 directions to try except for where
        it is coming from. [ example: if we took a step NORTH, then SOUTH is excluded 
        from future potential tries. ]
      - once a direction is tried, we add to the list of tries for the current position/node/vertex (x, y).
      - if the node's tries are exhausted N, W, E ... then backtrack 1 step
      - hmmm... we've been here before innit? oui ! mon Dieu ! 
      - in the node we backtracked to, check if we have any untried directions left.
      - if [ not ]: backtrack again. if [ yes ]: pop a move from remaining tries and go on your merry way.

      REPEAT

      '''
      
      if p not in tries:
          tries[p] = {self.reverse(move)}

      if len(tries[p]) < 4:
          backtrack = False

          move = nswe.difference(tries[p]).pop()
          tries[p].add(move)
          
      else:
          backtrack = True

          if not history: 
            '''
            no where to backtrack to. this will happen when we've explored 
            every other path and are forced to backtrack all the back to the beginning.

            END PROGRAM
            '''
            break

          move = self.reverse(history.pop())
          
      cpu.run(move)
      o = cpu.output()


      if o in {self.OK, self.OXYGEN_TANK_FOUND}:
        p = self.xy(move, p)
        self.__pos = p
        self.__bounds = self.update_bounds()

        if display: 
          self.display()

        if not backtrack:
            history.append(move)
            self.__map[p] = o
  
    return self.__map
      

  def reverse(self, direction = None):
    if direction == None: direction = self.__history[-1]
    
    return {
      self.MOV_NORTH : self.MOV_SOUTH, 
      self.MOV_SOUTH : self.MOV_NORTH, 
      self.MOV_WEST : self.MOV_EAST, 
      self.MOV_EAST : self.MOV_WEST
    }[direction]


  def xy(self, move, from_xy: tuple = None):
    x, y = from_xy if from_xy else self.__pos

    dnswe = {
      self.MOV_NORTH: (0, -1), 
      self.MOV_SOUTH: (0, 1), 
      self.MOV_WEST: (-1, 0), 
      self.MOV_EAST: (1, 0)
      }

    return tuple(a + b for a, b in zip((x, y), dnswe[move]))


  def update_bounds(self):
    mxy, xy = list(self.__bounds), self.__pos

    return tuple([min(p1, p2) for p1, p2 in zip(mxy[:2], xy)] + [max(p1, p2) for p1, p2 in zip(mxy[2:], xy)])


  def display(self):
    minx, miny, maxx, maxy = self.__bounds
    maxx, maxy = abs(minx) + maxx, abs(miny) + maxy
    px, py = self.__pos

    subprocess.call("clear")

    dash = 'Steps: {}, Max (x): {}, Max (y): {}'.format(len(self.__history), maxx, maxy)

    print(dash)
    print('.'*(maxx+1))

    grid = [[' ']*(maxx+1) for _ in range(maxy+1)]

    for (x, y), v in self.__map.items():
      x += abs(minx)
      y += abs(miny)

      if x < 0 or x > maxx or y < 0 or y > maxy: break

      try:
        grid[y][x] = self.__tiles[v]
      except:
        print('DEBUG', x, y, maxx, maxy)
        exit()
        break


    prev = grid[py+abs(miny)][px+abs(minx)]

    rx, ry = px+abs(minx), py+abs(miny)
    if prev != self.__tiles[self.OXYGEN_TANK_FOUND]:
      grid[ry][rx] = '🛸'
    else:
      grid[ry][rx-1] = '🛸'

    for l in grid: print(''.join(l))

    print('\n')
    print('.'*(maxx+1))
    print(dash)

    # sleep(0.1)


  def reset(self):
    if not self.__map: return

    self.__pos = (0, 0)

    self.__map = OrderedDict()
    self.__cpu = Machine(self.__m[:])
    if verbose: self.__cpu.toggle_verbose()

    return self






'''
Solution 1

'''

print('Solution 1 ----------------------------', '\n')
r = Droid(mreset[:])

print('BFS', shortest_path(r.map(True), (0, 0), Droid.OXYGEN_TANK_FOUND))

