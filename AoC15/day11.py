# @see https://adventofcode.com/2015/day/11

import re

seed = 'vzbxkghb'

alpha = {}
alpha_keys = 'abcdefghijklmnopqrstuvwxyz'
for i, k in enumerate(alpha_keys): alpha[k] = i

# Increment single "digit" in base 26
def increment_digit(d: str):
  res, rem = d, False
  if 25 == alpha[d]:
    res = alpha_keys[0]
    rem = True

  else:
    res = alpha_keys[alpha[d]+1]
    rem = False

  return res, rem

# Increment like counting with numbers. In this case we treat the password
# like a base 26 number!
def increment(pw: str):
  pwl = list(pw)

  # 8 digits, right to left
  for i in reversed(range(len(pw))):
    res, rem = increment_digit(pwl[i])
    pwl[i] = res

    # carry?
    if not rem:
      break
  
  return "".join(pwl)

# 1. Auto-fast-forward relevant letter positions if they match any of the letters i, o, or l
# 2. Example: The next password after ghijklmn is ghjaabcc, because you 
#    eventually skip all the passwords that start with ghi..., 
#    since i is not allowed.
def skip_iol(pw: str):
  for i in [7,6,5,4,3,2,1,0]:
    if pw[i] in 'iol':
      pw = increment(pw[:i+1]) + pw[i+1:]

  return pw

# Validate password and return True or False
def validate(pw: str):
  # Passwords may not contain the letters i, o, or l.
  if None != re.search(r'[iol]', pw) :
    return False

  # Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on.
  if None == re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', pw):
    return False

  # Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
  if None == re.search(r'([a-z])\1.*([a-z])\2', pw) :
    return False
  
  return True

# This is not pretty: incrementing old password string repeatedly until it is valid
def find_pw(pw: str):
  for _ in range(900000):
    if validate(pw): 
      break

    pw = skip_iol(increment(pw))

  return pw


print('------------ PART 01 -------------')
pw = find_pw(seed)
print('Next password:', pw)


print('\n------------ PART 02 -------------')
pw = find_pw(increment(pw))
print('Next password:', pw)