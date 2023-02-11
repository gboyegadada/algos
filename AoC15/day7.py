# @see https://adventofcode.com/2015/day/7

from lib.helper import filetolist
import re

def parse_line(l: str):
  res = re.search(r'^([a-z\d]+ )?([A-Z]+ )?([a-z\d]+) -> ([a-z]+)$', l).groups()

  in1 = res[0].strip() if None != res[0] else None
  in2 = res[2]
  operator = res[1].strip() if None != res[1] else None
  output = res[3]

  return in1, in2, operator, output 

def read(input: str, reg: dict):
  val = None

  if None == input:
    pass
  elif input.isnumeric():
    val = int(input)
  elif input in reg:
    val = reg[input]

  return val

# :notes
# Input 1 is the left side of a bitwise operation, e.g. in1 AND in2 -> out
# Input 2 is the right side of a bitwise operation (^^ see example ^^)
# Input 1 is not required in operations requiring only one input like: NOT in2 -> out, in2 -> out 
def exe(i1, i2, op: str, out: str, reg: dict, pending: dict):
  val1, val2 = read(i1, reg), read(i2, reg)

  # :if the output to input 1 is not available but expected
  if None == val1 and None != i1:
    pending[i1] = (i1, i2, op, out)

  # :if the output to input 2 is not yet available (input 2 is always expected)
  if None == val2:
    pending[i2] = (i1, i2, op, out)

  # :if both inputs are required but one or the other is unavailable, abort mission...
  if (None == val1 and None != i1) or None == val2:
    return reg, pending

  if 'AND' == op:
    reg[out] = val1 & val2

  elif 'OR' == op:
    reg[out] = val1 | val2

  elif 'NOT' == op:
    reg[out] = ~ val2

  elif 'LSHIFT' == op:
    reg[out]  = val1 << val2

  elif 'RSHIFT' == op:
    reg[out]  = val1 >> val2

  # This is an assignment
  elif None == op:
    reg[out] = val2

  # debug
  else:
    print('DEBUG NO-OP:', op, i1, i2, out)

  # :if there is an input waiting for this output.. 
  if out in pending:
    pi1, pi2, op, o = pending[out]
    
    # Remove output from pending list
    del pending[out]

    if out == pi1 and pi2 in reg:
      # Both inputs ready to compute
      reg, pending = exe(pi1, pi2, op, o, reg, pending)

    elif out == pi2 and (None == pi1 or pi1 in reg):
      # Both inputs ready or only input 2 is required and is ready to compute
      reg, pending = exe(pi1, pi2, op, o, reg, pending)

  return reg, pending

def part_one(d: list, reg: dict = {}, pending: dict = {}):

  for i1, i2, op, o in d:
    reg, pending = exe(i1, i2, op, o, reg, pending)

  # Do additional passes until there are no more
  # pending inputs...
  if len(pending) > 0:
    part_one(d, reg, pending)
  
  return reg['a']

def part_two(d: list, override: int):
  for i, (i1, i2, op, o) in enumerate(d):
    if 'b' == o:
      d[i] = (None, str(override), op, o)
      break
  
  return part_one(d, {}, {}) # Reset args because they somehow persist across separate calls :\

data = [parse_line(l) for l in filetolist('day7_input.txt', 'r')]

print('------------ PART 01 -------------')
a = part_one(data)
print('Signal is ultimately provided to wire a:', a)

print('\n------------ PART 02 -------------')
a = part_two(data, a)
print('Signal is ultimately provided to wire a:', a)