import math

# 1. Parse dimensions
def parse_dims(l: str):
  return [int(x) for x in l.split('x')]

# 2. Compute area of unique sides
def compute_unique_sides(d: list):
  return [d[0] * d[1], d[1] * d[2], d[0] * d[2]]

paper_sqft, ribbon_l = 0, 0

with open('day2_input.txt', 'r') as fp:
  for l in fp:
    d = parse_dims(l)
    s = compute_unique_sides(d)

    # 4. Compute wrapping paper area
    ss = min(s) # smallest side
    paper_sqft += 2 * sum(s) + ss

    # 5. Compute ribbon length    
    d.sort()
    ribbon_l += 2 * (d[0] + d[1]) + (d[0] * d[1] * d[2])


print('------------ PART 01 -------------')
print('Total square feet of wrapping paper: ', paper_sqft)


print('\n------------ PART 02 -------------')
print('Total feet of ribbon: ', ribbon_l)
  



