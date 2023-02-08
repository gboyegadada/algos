# @see https://adventofcode.com/2015/day/1

instructions = ''
with open('day1_input.txt', 'r') as fp:

  instructions = fp.readline()
  
# At what floor does Santa stop?
def last_floor(l: str):
  floor = 0
  for x in l:
    if x == '(':
      floor += 1
    else:
      floor -= 1

  return floor

# At which instruction does Santa enter the 
# basement for the first time?
def enters_basement_at(l: str):
  floor, steps = 0, 0
  for x in l:
    steps += 1
    if x == '(':
      floor += 1
    else:
      floor -= 1

    if floor == -1:
      break

  return steps
    
print('------------ PART 01 -------------')
print('Floor number: ', last_floor(instructions))


print('------------ PART 02 -------------')
print('Enters basement at: ', enters_basement_at(instructions))