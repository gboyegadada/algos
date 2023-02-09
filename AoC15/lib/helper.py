
import subprocess
from typing import Callable
from collections import deque

def stringify(m: dict, l: list):
  return ''.join([m.get(x) for x in l])

def filetolist(p: str, flag: str = 'r'):
  with open(p, flag) as f: 
    lines = [line.strip() for line in f]
    
  return lines