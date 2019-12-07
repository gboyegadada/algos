
import sys
import itertools

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]


class Machine:
  def __init__(self, m):
    self.memory = m
    self.pointer = 0
    self.len = len(m)
    self.out = 0
    self.__halt = False
    self.__initialized = False

  def input(self, v):
    self.run(v)

  def output(self):
    return self.out

  def halted(self):
    return self.__halt

  def initialized(self):
    return self.__initialized

  def run(self, input = None):

    if input != None:  
        self.__initialized = True

    while self.pointer < self.len:
      if self.len - self.pointer < 5: instr = self.memory + ([0] * 5) 
      else: instr = self.memory[:self.pointer+5]

      n = self.memory[self.pointer]
      op = n % 100
      m1 = n // 100 % 10
      m2 = n // 1000 % 10
      m3 = n // 10000 % 10

      p1, p2, p3 = instr[self.pointer+1], instr[self.pointer+2], instr[self.pointer+3]

      v1 = self.memory[p1] if m1 == 0 and op != 99 else p1
      v2 = self.memory[p2] if m2 == 0 and op not in {99,3,4} else p2
      v3 = self.memory[p3] if m3 == 0 and op in {1,2,7,8} else p3

      # 99: end
      if op == 99:
        self.__halt = True
        print('END')
        break

      # 1: sum
      elif op == 1:
        r = v1 + v2
        if m3 == 0: self.memory[p3] = r 
        else: self.memory[self.pointer+3] = r

        self.pointer += 4

      # 2: multiply
      elif op == 2:
        r = v1 * v2
        if m3 == 0: self.memory[p3] = r 
        else: self.memory[self.pointer+3] = r
        
        self.pointer += 4

      # 3: save to address
      elif op == 3: 
        if input == None:
          print('Waiting for input...')
          break # Wait for input...

        self.memory[p1] = input
        input = None
        
        print('READ:', self.memory[p1])
        self.pointer += 2

      # 4: output
      elif op == 4:
        print('OUTPUT: ', v1)
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
        
        if m3 == 0: self.memory[p3] = r 
        else: self.memory[self.pointer+3] = r

        self.pointer += 4

      # 8: equal
      elif op == 8: 
        r = 1 if v1 == v2 else 0
        
        if m3 == 0: self.memory[p3] = r 
        else: self.memory[self.pointer+3] = r

        self.pointer += 4

      else: 
        print('ERRRRR.....', self.pointer, op, self.memory[self.pointer:self.pointer+4])
        break

'''
PART 1

'''

result1, perms = 0, list(itertools.permutations(list(range(5)), 5))

for p in perms:
  m = [ 
    Machine(mreset[:]),
    Machine(mreset[:]),
    Machine(mreset[:]),
    Machine(mreset[:]),
    Machine(mreset[:]),
  ]

  _prev, _current = 4, 0

  while True:
      if m[_current].halted(): break

      if not m[_current].initialized(): m[_current].run(p[_current])
      else: m[_current].run(m[_prev].output())

      if _current == 4: 
         _prev = 4     
         _current = 0
      else:
        _prev = _current
        _current += 1

  print('SEQUENCE:', p, m[4].output())
  result1 = m[4].output() if m[4].output() > result1 else result1



'''
PART 2

'''

result2, perms = 0, list(itertools.permutations(list(range(5,10)), 5))

for p in perms:
  m = [ 
    Machine(mreset[:]),
    Machine(mreset[:]),
    Machine(mreset[:]),
    Machine(mreset[:]),
    Machine(mreset[:]),
  ]

  _prev, _current = 4, 0

  while True:
      if m[_current].halted(): break

      if not m[_current].initialized(): m[_current].run(p[_current])
      else: m[_current].run(m[_prev].output())

      if _current == 4: 
         _prev = 4     
         _current = 0
      else:
        _prev = _current
        _current += 1

  print('SEQUENCE:', p, m[4].output())
  result2 = m[4].output() if m[4].output() > result2 else result2


print('------ Part One ------')
print('MAX THRUST:', result1)


print('------ Part Two ------')
print('MAX THRUST:', result2)