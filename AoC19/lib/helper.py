
import subprocess

def neighbours(m: dict, pos: tuple, l: callable = lambda p, v: True):
  '''
  N (x, y), S (x, y), W (x, y), E (x, y)
  '''
  (x, y), dxy = pos, [(0, -1), (0, 1), (-1, 0), (1, 0)]

  n = [(x + dx, y + dy) for dx, dy in dxy]

  return [nn for nn in n if nn in m and l(nn, m.get(nn)) ]


def shortest(graph: dict, initial: tuple, target: any):
  '''
  parameters

  graph: our map in the shape { (x0,y0): value, (x1,y1): value, ... }
  initial: position (x, y)
  target: any value type
  '''
  
  visited = {initial: 1}
  queue = [initial]

  while queue:
      
      node = queue.pop(0)
      if graph.get(node, Droid.WALL) == target:
        return visited[node] - 1

      for neighbour in neighbours(graph, node, lambda p, v: v in {Droid.OK, Droid.OXYGEN} and p not in visited):
              
        visited[neighbour] = visited[node] + 1
        queue.append(neighbour)

  return -1

# print(shortest(rmap.copy(), (0,0), Droid.OXYGEN))


def display(m, bounds, clear: bool = False):
  maxx, maxy = bounds

  dash = f'Max (x): {maxx}, Max (y): {maxy}'

  if clear: subprocess.call("clear")

  print(dash)
  print('.'*maxx)

  grid = [[' ']*(maxx+1) for _ in range(maxy+1)]

  for (x, y), v in m.items():

    if x < 0 or x > maxx or y < 0 or y > maxy: break

    try:
      grid[y][x] = chr(v) if isinstance(v, int) else v 
    except Exception as err:
      print("Unexpected error:", err)
      print('DEBUG', x, y, maxx, maxy)
      exit()
      break

  for l in grid: print(''.join(l))

  print('.'*maxx)
  print(dash)