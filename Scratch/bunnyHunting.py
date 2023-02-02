import random

'''
- Bunny always moves P-1 or P+1 
- Bunny never stays in place

'''
bunny_pos_prev = 0
bunny_pos = 3

print('Initial pos:', bunny_pos)

search_pos_prev = 0
search_pos_curr = 0

def move_bunny():
  global bunny_pos_prev
  global bunny_pos

  bunny_pos_prev = bunny_pos

  if 0 == bunny_pos:
    # Initialise bunny pos
    bunny_pos = random.randint(1, 100)
    print('Bunny jumped from', bunny_pos_prev, 'to', bunny_pos)
    return

  # binary coin toss
  next = random.randint(0, 1)
  
  if 1 == bunny_pos:
    bunny_pos +=1

  elif 100 == bunny_pos:
    bunny_pos -= 1

  elif 0 == next and bunny_pos > 1:
    bunny_pos -= 1

  else:
    bunny_pos +=1
  
  print('Bunny jumped from', bunny_pos_prev, 'to', bunny_pos)

def find_bunny():
  global search_pos_curr
  global search_pos_prev
  global bunny_pos

  bunny_pos_curr = bunny_pos

  # This is the first iteration, no prev steps
  # We have double checked prev pos in case bunny hopped backwards
  if 0 == search_pos_curr or search_pos_prev == search_pos_curr:
    search_pos_curr += 1

  else:
    search_pos_prev = search_pos_curr

  return { 'found': bunny_pos_curr == search_pos_curr, 'guess': search_pos_curr }


while search_pos_curr < 100:
  move_bunny()
  res = find_bunny()

  if True == res['found']:
    print('YAYYYY !!', res)
    break

  else:
    print('Oooopss!', res)
