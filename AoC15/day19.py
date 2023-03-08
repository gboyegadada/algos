# @see https://adventofcode.com/2015/day/19

import re

data, initial = list(), str()

with open('day19_input.txt', 'r') as f: 
  for l in f:
    # H => HO
    r = re.match(r'([a-zA-Z]+) => ([a-zA-Z]+)', l.strip())

    if None != r:
      data.append((r[1], r[2]))

    elif len(l) > 1:
      initial = l.strip()

def replace(m: str, f: str, r: str, h: dict) -> tuple:
  """ Do a replacement and return new molecule and updated history 

  Args:
      m: the initial molecule
      f: find
      r: replace
      h: history
    Returns:
      m: new molecule
      h: updated history

  """
  k = f+r
  last_replaced_at = h[k] if k in h else -1
  
  i = m.find(f, last_replaced_at+1)

  if i > -1:
    h[k] = i
    
    m = m[0:i] + r + m[i+len(f):]

  return m, h

def part_one(d: list, i: str) -> int:
  """ Number of distinct molecules that can be created after all the 
      different ways you can do one replacement on the medicine molecule. 

  Args:
      d: possible replacements
      i: initial molecule
    Returns:
      number of distinct molecules

  """
  hist, molecules = dict(), set()
  for f, r in d:
    # print('| -------> matching: ', '(', f, ' => ', r, ') <---------- |')
    m, hist = replace(i, f, r, hist)

    while m != i:
      molecules.add(m)
      # print(m, '(', f, ' => ', r, ')')
      m, hist = replace(i, f, r, hist)

  return len(molecules)


print('------------ PART 01 -------------')
print('Number of distinct molecules that can be created:', part_one(data, initial))

print('\n------------ PART 02 -------------')
  


