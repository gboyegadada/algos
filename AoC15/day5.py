# @see https://adventofcode.com/2015/day/5

from lib.helper import filetolist
import re

words = filetolist('day5_input.txt')

def part1(w: list):
  n = 0
  for l in w:
    if re.search(r'([aeiou].*){3,}', l) and re.search(r'([a-z])\1+', l) and not re.search(r'(?:ab|cd|pq|xy)+', l):
      n += 1

  return n

def part2(w: list):
  n = 0
  for l in w:
    if re.search(r'([a-z][a-z]).*\1+', l) and re.search(r'([a-z])[a-z]\1+', l):
      n += 1

  return n

print('------------ PART 01 -------------')
nice = part1(words)
print('Matched', nice, 'nice strings')


print('\n------------ PART 02 -------------')
nice = part2(words)
print('Matched', nice, 'nice strings')
