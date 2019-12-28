import sys
from lib.intcode import Machine


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]

class SpringDroid:

  def __init__(self, m):
    self.__m = m
    self.__cpu = Machine(self.__m[:])

    if verbose: self.__cpu.toggle_verbose()

  
  def run(self, program):
    cpu = self.__cpu

    cpu.boot()
    cpu.run()

    self.out()


    for line in list(program):
      self.instruct(line, silent=True)

    self.instruct('WALK')


  def out(self, tostring: bool = True, silent: bool = False):
    cpu = self.__cpu

    o = []

    while cpu.has_output():
      b = cpu.output()
      o.append(b if b > 127 else chr(b))


    so = ''.join(map(str, o))

    if not silent: 
      print(so)

    return so if tostring else o

  
  def instruct(self, command: str, tostring: bool = True, silent: bool = False):
    '''
    - convert text command to ASCII and feed to computer.
    - return output
    '''

    if not silent: 
      print('INSTR:', command)

    cpu = self.__cpu

    for c in map(ord, command):
      cpu.run(c)
    
    cpu.run(10) # return

    return self.out(tostring, silent)

  

def one(d):
  '''
  Solution 1

  '''

  print('Solution 1 \n--------------------------------------------------')
  droid = SpringDroid(d)

  '''
  notes:
  -------------------------------
  1. droid jumps 4 steps at a time
  2. always check to see that tile D (4th tile) is solid (for landing)
  3. if you want to land on an island (###.##..####), jump 2 tiles before the first
     hole: so basically jump whenever C (3rd tile ahead) is a hole. 

  '''
  p = [
    'NOT C J',
    'AND D J',
    'NOT A T',
    'OR T J'
  ]

  droid.run(p)

  
def two(d):
  '''
  Solution 2

  '''
  print('Solution 2 \n--------------------------------------------------')


'''
Selector

'''

print('Select solution (enter 1 or 2 and press return):')
if 2 == int(sys.stdin.readline()): 
  two(mreset[:])
else: 
  one(mreset[:])
