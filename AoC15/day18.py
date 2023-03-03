# @see https://adventofcode.com/2015/day/18

grid = dict()
with open('day18_input.txt', 'r') as f: 
  y = 0
  for r in f:
    for x, v in enumerate(r.strip()):
      grid[(x, y)] = 1 if '#' == v else 0
    y += 1

def num_of_neighbours_on(x: int, y: int, g: dict):
    return  g.get((x, y-1), 0) + g.get((x+1, y-1), 0) + \
            g.get((x+1, y), 0) + g.get((x+1, y+1), 0) + \
            g.get((x, y+1), 0) + g.get((x-1, y+1), 0) + \
            g.get((x-1, y), 0) + g.get((x-1, y-1), 0)

def step(g: dict):
  gclone = dict(g)
  for x, y in g.keys():
    n = num_of_neighbours_on(x, y, g)
    # A light which is on stays on when 2 or 3 neighbors 
    # are on, and turns off otherwise...
    if 1 == g[x,y] and (2 != n and 3 != n):
      gclone[x,y] = 0

    # A light which is off turns on if exactly 3 neighbors are on, 
    # and stays off otherwise...
    elif 0 == g[x,y] and (3 == n):
      gclone[x,y] = 1
  
  return gclone

def part_one(g: dict):
  for _ in range(100):
    g = step(g)

  return sum(g.values())

def part_two(g: dict):
  for _ in range(100):
    g[0,0] = g[0,99] = g[99,0] = g[99,99] = 1 # ...four corners always in the on state

    g = step(g)

  g[0,0] = g[0,99] = g[99,0] = g[99,99] = 1 # ...four corners always in the on state

  return sum(g.values())

print('------------ PART 01 -------------')
print('Number of lights on:', part_one(grid))

print('\n------------ PART 02 -------------')
print('Number of lights on:', part_two(grid))
