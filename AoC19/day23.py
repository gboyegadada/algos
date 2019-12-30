import sys
from collections import deque
from lib.intcode import Machine


if len(sys.argv) == 1 or sys.argv[1] == '-v': 
  print('Input filename:')
  f=str(sys.stdin.readline()).strip()
else: f = sys.argv[1]

verbose = sys.argv[-1] == '-v'

for l in open(f):
  mreset = [int(x) for x in l.strip().split(',')]
  break


class Network:
  def __init__(self):
    self.__nodes = []


  def start(self):
    print(f'Starting network with {len(self.__nodes)} nodes!')
    print('==============================================')

    nat, prev_nat, first_packet = None, None, None
    

    while True:
      if verbose:
        print('Polling...')

      network_idle = True

      for i, n in enumerate(self.__nodes):
        machine, message_queue = n.values()
        

        '''
        1. deliver recieved packets
        '''
        if message_queue:
          network_idle = False

          for _ in range(2):
            machine.run(message_queue.popleft())

        else:
          machine.run(-1) # no messages


        '''
        2. pickup packets to send
        '''
        while machine.has_output():

          a, *d = self.read(machine)

          if verbose:
            print(f'packet from :{i} ===> :{a} |> x: {d[0]}, y: {d[1]}')
          
          if a == 255: 
            nat = d

            if not first_packet:
              first_packet = nat
              print('First packet to address 255: {{ x: {0}, y: {1} }}'.format(*first_packet))

            break
            

          self.send(a, d)


      if network_idle and nat:
          self.send(0, nat)

          if nat and prev_nat and nat[1] == prev_nat[1]:
            print('Consecutive Y sent to address 0:', nat[1])
            return

          prev_nat = nat
        

  def send(self, a, d: list):
    self.__nodes[a]['message_queue'] += d


  def read(self, n: Machine):
    o = []
    for _ in range(3):
      o.append(n.output())

    return o


  def add(self, node: Machine):
  
    if verbose: node.toggle_verbose()

    new_addr = len(self.__nodes)
    node.run(new_addr)
    
    self.__nodes.append({
      'machine': node,
      'message_queue': deque()
    })



'''
Solution 1 & 2
'''

net = Network()

for _ in range(50):
  node = Machine(mreset[:])

  net.add(node)

net.start()




  