import math

with open('day2_input.txt', 'r') as fp:

  l, mreset, count = fp.readline(), [], 0
  while l:
    mreset += str(l).split(',')
    
    count += 1
    l = fp.readline()

mreset = list(map(lambda x: int(x), mreset))

print('INPUT', count, mreset)

def run(m):
  p = 0
  while p+4 < len(m):
    if m[p] == 1:
      m[m[p+3]] = m[m[p+1]] + m[m[p+2]]
      p += 4

    elif m[p] == 2:
      m[m[p+3]] = m[m[p+1]] * m[m[p+2]]
      p += 4
    elif m[p] == 99:
      p += 1
      break

  return m


data = [x for x in mreset]
noun, verb = 0, 0
while noun <= 99:
  while verb <= 99:
    data = mreset[:]
    data[1] = noun
    data[2] = verb

    d = run(data)
    if d[0] == 19690720:
      
      print('OUTPUT', d[0:4], (100*noun+verb))
      break

    verb += 1

  if data[0] == 19690720: break

  noun += 1
  verb = 0

# m = list(map(lambda x: str(x), m))
# print('RES', n[0])