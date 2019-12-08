import sys
import itertools

if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

print('What is the image pixel width:')
w=int(sys.stdin.readline())

print('What is the image pixel height:')
h=int(sys.stdin.readline())
dim = w*h

layers, zeros = [], []

l = open(f, 'r').read().strip()
for i in range(0, len(l), dim): 
  layers.append(l[i:i + dim])
  zeros.append(layers[-1].count('0'))


'''
Part 1

'''

mz = zeros.index(min(zeros))
print('1.a. Layer {0} contains the fewest [0] digits.'.format(mz+1))

mult = layers[mz].count('1') * layers[mz].count('2')

print('1.b. Number of [1] digits * number of [2] digits ==', mult)


'''
Part 2

'''

# Trnsparent canvas
canvas = ' ' * len(layers[0])
li =  len(layers)-1
for i in range(li+1):
  
  canvas = ''.join([pixel if pixel != '2' else canvas[i] for i, pixel in enumerate(layers[li-i])])


print('\n2. ------- IMG ---------\n')
canvas = canvas.replace('1', '*').replace('0', ' ')
for j in range(0, len(canvas), w): 
  print(''.join(canvas[j:j + w]))
