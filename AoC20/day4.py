import sys
import re

if len(sys.argv) == 1: 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]


def is_valid_hgt(v):
  m = re.search(r'^(\d+)(cm|in)$', v)

  if m == None:
    return False

  q = int(m.group(1))
  u = m.group(2)

  return ('in' == u and q >= 59 and q <= 76) or ('cm' == u and q >= 150 and q <= 193)

def is_valid_yr(v, mn=1900, mx=3000):
  return len(v) == 4 and int(v) >= mn and int(v) <= mx

def is_valid_hcl(v):
  return True if re.match(r'^#[0-9a-f]{6}$', v) else False

def is_valid_ecl(v):
  return True if re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', v) else False

def is_valid_pid(v):
  return True if re.match(r'^\d{9}$', v) else False


def is_valid(s, strict=False):
  has_required_fields = 'byr' in s and 'iyr' in s and 'eyr' in s and 'hgt' in s and 'hcl' in s and 'ecl' in s and 'pid' in s

  if not has_required_fields:
    return False

  if strict:
    p = dict([x.split(':') for x in s.strip().split(' ')])

    pid_valid_if_present =  is_valid_pid(p['pid']) if p.has_key('pid') else True
    other_fields_valid = has_required_fields and is_valid_yr(p['byr'], 1920, 2002) and is_valid_yr(p['iyr'], 2010, 2020) and is_valid_yr(p['eyr'], 2020, 2030) and is_valid_hgt(p['hgt']) and is_valid_hcl(p['hcl']) and is_valid_ecl(p['ecl'])

    valid = pid_valid_if_present and other_fields_valid
  else:
    valid = True

  return valid


buffer = ''
valid = 0
valid_strict = 0

for l in open(f):
  s = l.strip()

  if len(s) > 0: 
    buffer += s + ' '
  else:
    valid += (1 if is_valid(buffer) else 0)
    valid_strict += (1 if is_valid(buffer, True) else 0)
    buffer = ''

# Check for leftover in buffer, process, and clear.
if len(buffer) > 0:
    valid += (1 if is_valid(buffer) else 0)
    valid_strict += (1 if is_valid(buffer, True) else 0)
    buffer = ''


'''
Solution 1

'''
print('Solution 1:', valid)


'''
Solution 2

'''
print('Solution 2:', valid_strict)