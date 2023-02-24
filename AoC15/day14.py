# @see https://adventofcode.com/2015/day/14

# Note: 
# -----------------------------------------------------------
# I apologise in advance to you (or to my future self) if this  
# isn't readable enough :/

import re

def parse_line(s: str):
  r = re.match(r'([A-Z][a-z]+) can fly ([\d]+) km/s for ([\d]+) seconds, but then must rest for ([\d]+) seconds.', s.strip())

  return r[1], r[2], r[3], r[4] # name, speed, burst, rest

with open('day14_input.txt', 'r') as f: 
  reindeers = list()
  for l in f:
    n, speed, burst, rest = parse_line(l) 
    reindeers.append({'name': n, 'speed': int(speed), 'burst': int(burst), 'rest': int(rest)})


def calc_dist_covered(speed: int, burst: int, rest: int, t: int):
  dist = speed * burst * int(t / (burst + rest))
  rem = t % (burst + rest)
  dist += speed * (rem if rem <= burst else burst)

  return dist

def calc_winning_dist(data: list, t: int):
  wd = 0
  for x in data:
    wd = max(wd, calc_dist_covered(x['speed'], x['burst'], x['rest'], t))

  return wd

# List of leading reindeers at a giving time t
def leading_at_t(data: list, t: int):
  # 1. Distance covered is mapped to contestants in reverse 
  # 2. The key is the distance covered, the value is a list of contestants
  # 3. Multiple contestants might cover the same distance at time t
  # 4. Structure should look like so:
  #    {23: ['Comet', 'Dancer'], 17: ['Cupid'], 10: ['Dasher', 'Donner']} 
  leaderboard = dict()
  for x in data:
    d = calc_dist_covered(x['speed'], x['burst'], x['rest'], t)
    if d in leaderboard:
      leaderboard[d].append(x['name'])
    else:
      leaderboard[d] = [x['name']]

  return leaderboard[max(leaderboard.keys())]

def overall_winner(data: list, tt: int):
    # Initialise our leaderboard...
    # key is contestant's name, value is points accumulated
    leaderboard = dict()
    for rd in data: leaderboard[rd['name']] = 0

    for t in range(1, tt+1):
      for k in leading_at_t(data, t):
        leaderboard[k] += 1

    return max(leaderboard.values())

# Duration of contest
time_t = 2503

print('------------ PART 01 -------------')
print('Winning reindeer traveled:', calc_winning_dist(reindeers, time_t), 'km')

print('\n------------ PART 02 -------------')
print('Winning reindeer has:', overall_winner(reindeers, time_t), 'points')