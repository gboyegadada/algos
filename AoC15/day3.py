data = ''
with open('day3_input.txt', 'r') as fp:
  data = fp.readline()

def santa_alone(instructions: str):
  v = {(0, 0)} # ...visited
  x, y = 0, 0 # ...Santa's last step

  for step in instructions:
    if '^' == step:
      y += 1
    elif 'v' == step:
      y -= 1
    elif '>' == step:
      x += 1
    elif '<' == step:
      x -= 1
    v.add((x, y))

  return v

def with_robo_santa(instructions: str):
  v = {(0, 0)} # ...visited
  x, y = 0, 0 # ...Santa's last step
  xb, yb = 0, 0 # ...bots's last step
  santa_is_next = True

  for step in instructions:
    if santa_is_next:
      if '^' == step:
        y += 1
      elif 'v' == step:
        y -= 1
      elif '>' == step:
        x += 1
      elif '<' == step:
        x -= 1
      v.add((x, y))

    else:
      if '^' == step:
        yb += 1
      elif 'v' == step:
        yb -= 1
      elif '>' == step:
        xb += 1
      elif '<' == step:
        xb -= 1
      v.add((xb, yb))

    santa_is_next = not santa_is_next

  return v

print('------------ PART 01 -------------')
print('With Santa by himself,', len(santa_alone(data)), 'houses receive at least one present.')


print('\n------------ PART 02 -------------')
print('With Robo-Santa by his side,', len(with_robo_santa(data)), 'houses receive at least one present.')
  


