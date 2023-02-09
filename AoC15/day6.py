# @see https://adventofcode.com/2015/day/6

from lib.helper import filetolist
import re


data = filetolist('day6_input.txt', 'r')


def parse_line(l: str):
  res = re.search(r'^(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)$', l).groups()

  s = 0 # turn off
  if 'turn on' == res[0]:
    s = 1
  elif 'toggle' == res[0]:
    s = 2

  return s, (int(res[1]),int(res[2])), (int(res[3]),int(res[4]))

def update_range(c1: tuple, c2: tuple, g: dict, s: int):
  for x in range(c1[0], c2[0]+1):
    for y in range(c1[1], c2[1]+1):

      # :if we are to "turn off" or "toggle" a light that used to be "on"
      if (0 == s or 2 == s) and (x, y) in g:
        del g[(x, y)] # Remove positions where light is "off"

      # :if we are to "turn on" or "toggle" a light that used to be "off"
      elif 1 == s or (2 == s and (x, y) not in g):
        g[(x, y)] = True # Set positions where light is "on"

  return g


def update_brighness(c1: tuple, c2: tuple, g: dict, s: int):
  for x in range(c1[0], c2[0]+1):
    for y in range(c1[1], c2[1]+1):

      # :init
      if (x, y) not in g:
        g[(x, y)] = 0

      # :if we are to "turn off", decrease brightness by 1 to minimum of 0
      if 0 == s and g[(x, y)] > 0:
        g[(x, y)] -= 1

      # :if we are to "turn on", increase brightness by 1
      elif 1 == s:
        g[(x, y)] += 1

      # :if we are to "toggle", increase brightness by 2
      elif 2 == s:
        g[(x, y)] += 2

  return g


def part_one(d: list):
  # We will only set co-ords of lights that are "on" so it is easy to count
  # how many are "on" simply by using len()
  grid = {}
  for l in d:
    on_or_off, c1, c2 = parse_line(l.strip())
    grid = update_range(c1, c2, grid, on_or_off)

  return len(grid)

def part_two(d: list):
  # This time, we have to keep all co-ords in the instructions
  # then do a sum() of the values()
  grid = {}
  for l in d:
    on_or_off, c1, c2 = parse_line(l.strip())
    grid = update_brighness(c1, c2, grid, on_or_off)

  return sum(grid.values())


print('------------ PART 01 -------------')
print('Number of lights on:', part_one(data))


print('\n------------ PART 02 -------------')
print('Total brightness:', part_two(data))