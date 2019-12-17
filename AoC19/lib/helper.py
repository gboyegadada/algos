
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

print(shortest(rmap.copy(), (0,0), Droid.OXYGEN))