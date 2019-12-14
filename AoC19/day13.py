import sys
from collections import defaultdict
from lib.intcode import Machine
import subprocess


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]

class Arcade9000Turbo:
  def __init__(self, m):
    self.__cpu = Machine(m)
    self.__minx = self.__miny = self.__maxx = self.__maxy = 0

    '''
    we only need to track (x)
    '''
    self.__player_x = 0
    self.__ball_x = 0
    self.__canvas = defaultdict(lambda: ' ')
    self.__scores = 0
    self.__tiles = {
      0: ' ',
      1: '|',
      2: '⬜',
      3: '➖',
      4: '⚪'
    }

    if verbose: self.__cpu.toggle_verbose()

  def play(self, auto: bool = False):
    self.__cpu.run()

    while not self.__cpu.halted() or self.__cpu.has_output():
      x = self.__cpu.output()
      y = self.__cpu.output()

      if x == -1 and y == 0:
        '''
        player's current score

        '''
        self.__scores = self.__cpu.output()
        self.display()
      
      elif x != None and y != None:
        '''
        draw a tile to the screen

        '''
        self.draw(x, y, self.__cpu.output())
        self.display()

      elif auto and self.__cpu.waiting(): 
        m = 0
        if self.__ball_x > self.__player_x: 
          m = 1
          print('_/_ >')
        
        elif self.__ball_x < self.__player_x: 
          m = -1
          print('_\\_ >')
        else:
          print('_|_ >')

        self.__cpu.run(m)

      elif self.__cpu.waiting(): 
        print('_|_ >')
        self.input()



  def input(self):
      try:
        self.__cpu.run(int(sys.stdin.readline()))
      except ValueError:
        print('Invalid input (hint: enter -1, 0, or 1 ):')
        self.input()

  def display(self):
    grid = [[' ']*(self.__maxx+1) for _ in range(self.__maxy+1)]

    count = 0
    for (x, y), v in self.__canvas.items():
      if x < 0 or y < 0: break
      if v == self.__tiles[2]: count += 1
      grid[y][x] = v

    subprocess.call("clear")
    for l in grid: print(''.join(l))

    print('\n')
    print('.'*(self.__maxx+1))

    print('Score: {0}, Blocks: {1}'.format(self.__scores, count))

  def draw(self, x, y, tile_id):
    self.__canvas[(x, y)] = self.__tiles[tile_id]

    self.__minx = min(self.__minx, x)
    self.__maxx = max(self.__maxx, x)
    self.__miny = min(self.__miny, y)
    self.__maxy = max(self.__maxy, y)

    if tile_id == 4:
      '''
      track ball displacement
      '''
      self.__ball_x = x
    elif tile_id == 3:
      '''
      track player position
      '''
      self.__player_x = x


'''
Solution 1

'''
def one(mreset):
  print('Solution 1 ----------------------------', '\n')
  arcade = Arcade9000Turbo(mreset[:])
  arcade.play()



'''
Solution 2

'''
def two(mreset):
  print('Solution 2 ----------------------------', '\n')
  jailbreak = mreset[:]
  jailbreak[0] = 2
  arcade = Arcade9000Turbo(jailbreak)
  arcade.play(False)



'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two(mreset)
else: 
  one(mreset)
