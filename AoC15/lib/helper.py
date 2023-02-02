
import subprocess
from typing import Callable
from collections import deque
import re

def stringify(m: dict, l: list):
  return ''.join([m.get(x) for x in l])
