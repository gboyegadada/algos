# @see https://adventofcode.com/2015/day/3

data = ''
with open('day3_input.txt', 'r') as fp:
  data = fp.readline()

def step(s: str, x: int, y: int):
    if '^' == s:
      y += 1
    elif 'v' == s:
      y -= 1
    elif '>' == s:
      x += 1
    elif '<' == s:
      x -= 1
    
    return x, y

def santa_alone(instructions: str):
  v = {(0, 0)} # ...visited
  x, y = 0, 0 # ...Santa's last step

  for s in instructions:
    x, y = step(s, x, y)
    v.add((x, y))

  return v

def with_robo_santa(instructions: str):
  v = {(0, 0)} # ...visited
  x, y = 0, 0 # ...Santa's last step
  xb, yb = 0, 0 # ...bots's last step
  santas_turn = True

  for s in instructions:
    if santas_turn:
      x, y = step(s, x, y)
      v.add((x, y))

    else:
      xb, yb = step(s, xb, yb)
      v.add((xb, yb))

    santas_turn = not santas_turn

  return v

print('------------ PART 01 -------------')
print('With Santa by himself,', len(santa_alone(data)), 'houses receive at least one present.')


print('\n------------ PART 02 -------------')
print('With Robo-Santa by his side,', len(with_robo_santa(data)), 'houses receive at least one present.')
  


