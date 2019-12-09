
import sys
import itertools

if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]


class Machine:
  def __init__(self, m):
    self.memory = m + [0]*80000
    self.pointer = 0
    self.relative_base = 0
    self.len = len(m)
    self.out = 0
    self.__halt = False
    self.__initialized = False

  def input(self, v):
    self.run(v)

  def output(self):
    return self.out

  def get_memory(self):
    return self.memory

  def halted(self):
    return self.__halt

  def initialized(self):
    return self.__initialized

  def run(self, input = None):

    if input != None:  
        self.__initialized = True

    while self.pointer < self.len:
      n = self.memory[self.pointer]
      op, m = n % 100, [ n // 100 % 10, n // 1000 % 10, n // 10000 % 10 ]

      p, v = self.memory[self.pointer+1:self.pointer+4], [0]*3

      for i in range(3):
        if m[i] == 0: 
          v[i] = self.memory[p[i]] 
        elif m[i] == 2: 
          p[i] = self.relative_base + p[i]
          v[i] = self.memory[p[i]] 
        else: 
          v[i] = p[i]
          p[i] = self.pointer + i + 1

      ''' 
      For convenience: pn for positions, vn for values 
      '''
      p1, p2, p3 = p
      v1, v2, v3 = v

      # 99: end
      if op == 99:
        self.__halt = True
        if verbose: print('END')
        break

      # 1: sum
      elif op == 1:
        r = v1 + v2
        self.memory[p3] = r 

        self.pointer += 4

      # 2: multiply
      elif op == 2:
        r = v1 * v2
        self.memory[p3] = r
        
        self.pointer += 4

      # 3: save to address
      elif op == 3: 
        if input == None:
          if verbose: print('Waiting for input...')
          break # Wait for input...

        self.memory[p1] = input 
        if verbose: print('READ:', self.memory[p1])

        input = None
        
        
        self.pointer += 2

      # 4: output
      elif op == 4:
        if verbose: print('OUTPUT: ', v1)
        self.out = v1

        self.pointer += 2

      # 5: jump-if-true
      elif op == 5: 
        if v1 != 0: self.pointer = v2
        else: self.pointer += 3

      # 6: jump-if-false
      elif op == 6: 
        if v1 == 0: self.pointer = v2
        else: self.pointer += 3

      # 7: less than
      elif op == 7: 
        r = 1 if v1 < v2 else 0
        
        self.memory[p3] = r

        self.pointer += 4

      # 8: equal
      elif op == 8: 
        r = 1 if v1 == v2 else 0
        
        self.memory[p3] = r 

        self.pointer += 4

      # 9: set relative base
      elif op == 9: 
        self.relative_base += v1

        self.pointer += 2

      else: 
        print('ERRRRR.....', self.pointer, op, self.memory[self.pointer:self.pointer+4])
        break


print('------------- PART 1 ----------------')
intcode = Machine(mreset[:])
intcode.run(1)

print('------------- PART 2 ----------------')
intcode = Machine(mreset[:])
intcode.run(2)