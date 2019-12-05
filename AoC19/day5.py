import math
import sys

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

with open(f, 'r') as fp:

  l, mreset, string = fp.readline(), [], ''
  while l:
    string += str(l) #.strip()
    
    l = fp.readline()

mreset = [int(x) for x in string.split(',')]

def run(m, id: int):
  p, lenm = 0, len(m)

  while p < lenm:
    if lenm-p < 5: instr = m + ([0] * 5) 
    else: instr = m[:p+5]

    n = m[p]
    op = n % 100
    m1 = n // 100 % 10
    m2 = n // 1000 % 10
    m3 = n // 10000 % 10

    p1, p2, p3 = instr[p+1], instr[p+2], instr[p+3]

    v1 = m[p1] if m1 == 0 and op != 99 else p1
    v2 = m[p2] if m2 == 0 and op not in {99,3,4} else p2
    v3 = m[p3] if m3 == 0 and op in {1,2,7,8} else p3


    # 99: end
    if op == 99:
      print('END')
      break

    # 1: sum
    elif op == 1: # or op == 0:
      r = v1 + v2
      if m3 == 0: m[p3] = r 
      else: m[p+3] = r

      p += 4

    # 2: multiply
    elif op == 2:
      r = v1 * v2
      if m3 == 0: m[p3] = r 
      else: m[p+3] = r
      
      p += 4

    # 3: save to address
    elif op == 3: 
      m[p1] = id
      
      p += 2

    # 4: output
    elif op == 4:
      print('OUTPUT: ', v1, p1)
      p += 2

    # 5: jump-if-true
    elif op == 5: 
      if v1 != 0: p = v2
      else: p += 3

    # 6: jump-if-false
    elif op == 6: 
      if v1 == 0: p = v2
      else: p += 3

    # 7: less than
    elif op == 7: 
      r = 1 if v1 < v2 else 0
      
      if m3 == 0: m[p3] = r 
      else: m[p+3] = r

      p += 4

    # 8: equal
    elif op == 8: 
      r = 1 if v1 == v2 else 0
      
      if m3 == 0: m[p3] = r 
      else: m[p+3] = r

      p += 4

    else: 
      print('ERRRRR.....', p, op, m[p:p+4])
      break

  return m

# noun, verb = 12, 2
# data[1] = noun
# data[2] = verb

print(' ----------- RUN -------- ')
print('Provide Sytem ID:')
id=int(sys.stdin.readline())
result = run(mreset[:], id)
