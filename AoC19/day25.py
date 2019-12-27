import sys
from itertools import combinations
from lib.intcode import Machine
import re
from time import sleep


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]


class Bot:
  NORTH = 'north'
  SOUTH = 'south'
  WEST = 'west'
  EAST = 'east'

  def __init__(self, m):
    self.__m = m
    self.__cpu = Machine(self.__m[:])
    self.__history = []
    
    self.__move_count = 0
    self.__safe_items = {'asterisk', 'polygon', 'tambourine', 'mug', 'cake', 'jam', 'easter egg', 'klein bottle'}

    if verbose: self.__cpu.toggle_verbose()


  def map(self, _display = True):

    history = self.__history
    p = 0
    move = self.NORTH
    tries = {}
    inventory = set()
    seen_items = set()
    safe_items = self.__safe_items
    checkpoint_map = []
    disable_pickups = False

    self.__cpu.run()
    o = ''.join(list(map(chr, self.__cpu.dump_output(clear=True))))

    print('MAIN OUTPUT:', o)


    while True and not self.__cpu.halted():
      sleep(0.2)

      '''
      here, we will use (D)epth (F)irst (S)earch algo to traverse
      the entire map, collect all items and find our way to the checkpoint.

      '''
      p = self.location(o)

      if p not in tries:
        tries[p] = set(self.moves(o))

      if tries[p]:
          print(f'AVAILABLE TRIES FOR [ {p.upper()} ]:', tries[p])
          backtrack = False

          prev = move
          move = tries[p].pop()

          if tries[p] and prev == self.reverse(move):
            prev = move
            move = tries[p].pop()
            tries[p].add(prev)
          
      else:
          backtrack = True

          if not history: 
            '''
            no where to backtrack to. this will happen when we've explored 
            every other path and are forced to backtrack all the back to the beginning.

            END PROGRAM
            '''
            print('NO HISTORY')

            if checkpoint_map and len(seen_items) == len(safe_items):
                print('ALL SET: NAVIGATE TO CHECKPOINT')
                print('SEEN ITEMS:', seen_items)
                print('Hit enter to continue >_')
                
                sys.stdin.readline()

                path = checkpoint_map[::-1]

                while path:
                  self.instruct(path.pop())

                move = self.EAST

            else:
              print('MISSING ITEMS OR NO CHECKPOINT PATH')
              print('PATH:', checkpoint_map)
              print('SEEN ITEMS:', seen_items)
              break

          else:
            move = self.reverse(history.pop())

      o = self.instruct(move)

      
      for item in self.items(o):
        if item not in 'molten lava escape pod giant electromagnet photons infinite loop' and (not disable_pickups or item not in seen_items):
          self.instruct(f'take {item}')
          inventory.add(item)
          seen_items.add(item)

        else:
          pass # print('SKIPPED:', item)

      if 'checkpoint' in o:
        print('CHECKPOINT')

        '''
        Save path to checkpoint for later
        '''
        checkpoint_map = history.copy()

        ''' 
        Make sure ALL safe items are collected before 
        initiating brute force.
        '''
        if len(seen_items) != len(safe_items):
          continue

        else:
          print('============ ALL SET ================')
          self.instruct('inv')
          print('=====================================')
          print('Hit enter to continue >_')

          sys.stdin.readline()

          self.brute()
          break


      if "You can't go that way" not in o:

        if not backtrack:
            history.append(move)



  def brute(self):
    '''
    try all possible combinations of items at the checkpoint.
    '''

    for i in range(3, 6):
      print(f'TRYING SETS OF {i}')
      print('-------------------------------------')
      print('Hit enter to continue >_')
      sys.stdin.readline()

      item_combinations = set(combinations(self.__safe_items, i))
    
      while item_combinations:
        current_set = item_combinations.pop()
        print('TRYING WITH FOLLOWING INVENTORY:', current_set)

        _o = self.items(self.instruct('inv', silent=True))

        for item in [x for x in _o if x not in current_set]:
          self.instruct(f'drop {item}', silent=True)

        for item in [x for x in current_set if x not in _o]:
          self.instruct(f'take {item}', silent=True)

        _o = self.instruct('inv')

        ''' TRY '''
        _o = self.instruct('east')

        if not re.search(r'(heavier|lighter) than', _o):
          print('YAYYYY (?):', _o)
          return

        sleep(0.2)

    print('SECURITY BREACH FAILED. TRY AGAIN.')

  
  def instruct(self, command: str, join: bool = True, silent: bool = False):
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

    o = list(map(chr, cpu.dump_output(clear=True)))

    if not silent: 
      print('OUTPUT:', ''.join(o))

    return ''.join(o) if join else o

  
  def moves(self, o):
    '''
    extract available moves from output
    '''

    res = re.findall(r'- (north|south|east|west)', ''.join(o))

    if res: 
      pass # print('MOVES:', res)

    return res

  
  def items(self, o):
    '''
    extract items from output
    '''

    res = re.findall(r'- ([ a-z]+)', o)

    if res: 
      res = [x for x in res if x not in {'north', 'south', 'east', 'west'}]
      # if res: print('ITEMS:', res)

    return res

  
  def location(self, o):
    '''
    extract location from output
    '''

    res = re.findall(r'== ([ a-z]+) ==', o.lower())


    return res[0]


  def reverse(self, direction = None):
    if direction == None: direction = self.__history[-1]
    
    return {
      self.NORTH : self.SOUTH, 
      self.SOUTH : self.NORTH, 
      self.WEST : self.EAST, 
      self.EAST : self.WEST
    }[direction]



def one(d):
  '''
  Solution 1

  '''

  print('Solution 1 \n--------------------------------------------------')
  robo = Bot(d)
  robo.map(True)

  
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
