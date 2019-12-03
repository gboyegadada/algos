import math

total, count = 0, 0


def calc(mass: int):
    f = (math.floor(mass / 3) - 2)

    return f + calc(f) if f > 0 else 0
    
with open('day1_input.txt', 'r') as fp:

  l = fp.readline()
  while l:
    mass = int(l)

    total += calc(mass)
    count += 1

    l = fp.readline()

print(total, count)