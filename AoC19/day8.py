import sys

if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

print('What is the image pixel width?')
w = int(sys.stdin.readline())

print('What is the image pixel height?')
h = int(sys.stdin.readline())
dim = w * h

canvas, zeros, ones, twos = ' ' * dim, [], [], []

l = open(f, 'r').read().strip()
for i in range(len(l), 0, -dim): 
  layer = l[i - dim:i]

  canvas = [pixel if pixel != '2' else canvas[j] for j, pixel in enumerate(layer)]
  zeros.append(layer.count('0'))
  ones.append(layer.count('1'))
  twos.append(layer.count('2'))


'''
Part 1

'''

mz = zeros.index(min(zeros))
print('1.a. Layer {0} contains the fewest [0] digits.'.format(mz))

mult = ones[mz] * twos[mz]
print('1.b. Number of [1] digits * number of [2] digits ==', mult)


'''
Part 2

'''

print('\n2. ------- IMG ---------\n')
canvas = ''.join(canvas).replace('1', '*').replace('0', ' ')
for p in range(0, len(canvas), w): 
  print(''.join(canvas[p:p + w]))
