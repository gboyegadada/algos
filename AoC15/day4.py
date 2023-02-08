# @see https://adventofcode.com/2015/day/4

from hashlib import md5

key = 'iwrupvqb'

def search(z: int, k: str = key, start: int = 0):
  d, n, zs = None, None, ''.zfill(z)
  for x in range(start, 99999999):
    s = key + str(x)
    d = md5(s.encode()).hexdigest()

    if zs == d[0:z]:
      n = x
      break
      
  return d, n


print('------------ PART 01 -------------')
d, n = search(5)
print('5 zeros with key [', key, '], matched [', d, '] at [', n, ']')


print('\n------------ PART 02 -------------')
d, n = search(6)
print('6 zeros with key [', key, '], matched [', d, '] at [', n, ']')