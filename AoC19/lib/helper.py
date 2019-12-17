
def neighbours(m, pos: tuple):
  '''
  N (x, y), S (x, y), W (x, y), E (x, y)
  '''
  (x, y), dxy = pos, [(0, -1), (0, 1), (-1, 0), (1, 0)]

  n = [(x + dx, y + dy) for dx, dy in dxy]

  return [nn for nn in n if nn in m]

def shortest_path(g: dict, sv, t):
  '''
  starting position of droid 
  '''
  sv = (0, 0)

  '''
  + q.append()
  + q.pop(0)
  '''
  q, explored = [[sv]], set()

  while q:
    path = q.pop(0)
    n = path[-1]

    if g.get(n) == t:
      
      return len(path) - 1
    
    if n in explored: continue

    explored.add(n)
    for nn in neighbours(g, n):
      new_path = path.copy()
      new_path.append(nn)
      q.append(new_path)

  return -1

def max_min_xy(mxy, xy):
  mxy = list(mxy)
  return tuple([min(p1, p2) for p1, p2 in zip(mxy[:2], xy)] + [max(p1, p2) for p1, p2 in zip(mxy[2:], xy)])

