import math
import re
from typing import List, Any

n1, n2 = 178416, 676461

repeats = [(str(i) * 2, str(i) * 3) for i in range(10)]

def any_repeats(n): 
  s = str(n)
  return any(d in s and not t in s for d, t in repeats)

def sortCheck(n):
  return str(n) == ''.join(sorted(list(str(n))))

opt = [ n for n in range(n1, n2+1) if any_repeats(n) and sortCheck(n)]

# Yield successive n-sized 
# chunks from l. 
# def pchunks(l, n): 
#     # looping till length l 
#     for i in range(0, len(l), n):  
#         print(l[i:i + n])

# pchunks(opt, 12)

print('ANS:', len(opt))

