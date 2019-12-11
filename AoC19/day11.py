import sys
from collections import defaultdict
from lib.intcode import Machine


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]

class Robot:
  def __init__(self, m):
    self.__cpu = Machine(m)

    '''
    {current, min, max}

    '''
    self.__x, self.__y = (0, 0, 0), (0, 0, 0)
    self.__panels = defaultdict(lambda: '.')
    self.__color = 0

    '''
    < : 0
    ^ : 1
    > : 2
    v : 3

    '''
    self.__direction = 1

    if verbose: self.__cpu.toggle_verbose()


  def start(self, start_color):
    if start_color: self.__panels[(0, 0)] = '#'

    while not self.__cpu.halted():

      self.__cpu.run(1 if self.__panels[(self.__x[0], self.__y[0])] == '#' else 0)

      self.paint(self.__cpu.output())

      self.turn(self.__cpu.output())
      self.move()


  def display(self):
    _, minx, maxx = self.__x
    _, miny, maxy = self.__y


    grid = [[' ']*(maxx+1) for _ in range(maxy+1)]

    for (x, y), v in self.__panels.items():
      if x < 0 or y < 0: break

      if v == '#': grid[y][x] = v

    for l in grid: print(''.join(l))
    
    print('\n', '--------------------------------------\n', 'COUNT', len(self.__panels), '\n\n')

  def turn(self, lr):
    if verbose: print('FROM ', ['<', '^', '>', 'v'][self.__direction]*4, lr)
    if lr == 0: self.left()
    else: self.right()

    if verbose: print('TURNED ', ['<', '^', '>', 'v'][self.__direction]*4)


  def left(self):
    self.__direction += (3 if self.__direction == 0 else -1)

    return self.__direction

  def right(self):
    self.__direction += (-3 if self.__direction == 3 else 1)

    return self.__direction

  def move(self):
    x, minx, maxx = self.__x
    y, miny, maxy = self.__y

    # <- left
    if self.__direction == 0: 
      if verbose: print('MOV <----', x)
      x -= 1
      minx = min(minx, x)

      if verbose: print('x:', x)

    # -> right
    elif self.__direction == 2: 
      if verbose: print('MOV ---->', x)
      x += 1
      maxx = max(maxx, x)

      if verbose: print('x:', x)

    # -> up
    elif self.__direction == 1: 
      if verbose: print('MOV ^^^^^^', y)
      y -= 1
      miny = min(miny, y)

      if verbose:  print('y:', y)

    # -> down
    elif self.__direction == 3: 
      if verbose: print('MOV vvvvvv', y)
      y += 1
      maxy = max(maxy, y)
        
      if verbose: print('y:', y)

    self.__x, self.__y = (x, minx, maxx), (y, miny, maxy)
      

  def paint(self, color = None):
    if color != None: self.__color = color
  

    self.__panels[(self.__x[0], self.__y[0])] = ('.' if self.__color == 0 else '#') 



'''
Solution 1

'''

print('Solution 1 ----------------------------', '\n')
r = Robot(mreset[:])
r.start(0)
r.display()


'''
Solution 2

'''

print('Solution 2 ----------------------------', '\n')
r = Robot(mreset[:])
r.start(1)
r.display()
