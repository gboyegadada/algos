# @see https://adventofcode.com/2015/day/8

from lib.helper import filetolist
import re

def count_chars_in_mem(l: str):
  res = re.findall(r'(\\\\|\\"|\\x[a-z0-9][a-z0-9]|[a-z"])', l)

  return len(res) - 2

def escape(s: str):
  return '"' + re.sub(r'(["\\])', r'\\\1', s) + '"'

def part_one(d: list):
  code_acc, mem_acc = 0, 0
  for l in d:
    code_acc += len(l)
    mem_acc += count_chars_in_mem(l)

  return code_acc - mem_acc

def part_two(d: list):
  new_code_acc, og_code_acc = 0, 0
  for l in d:
    og_code_acc += len(l)
    new_code_acc += len(escape(l))

  return new_code_acc - og_code_acc


data = filetolist('day8_input.txt', 'r')

print('------------ PART 01 -------------')
print('The number of chars of code for string literals minus the number of chars in memory:', part_one(data))

print('\n------------ PART 02 -------------')
print('The number of chars in newly encoded strings minus the number of chars in the original:', part_two(data))
