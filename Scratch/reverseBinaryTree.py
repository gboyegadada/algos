def reverseNode(node: dict):
  # { value: x, left: {...}, right: {...} }
  new_left = reverseNode(node['right']) if node['right'] is not None else None
  new_right = reverseNode(node['left']) if node['left'] is not None else None

  node['left'] = new_left
  node['right'] = new_right

  return node

def printNode(n: dict):
  print(n['value'])

  if n['left']is not None: printNode(n['left'])
  if n['right']is not None: printNode(n['right'])

n = {
      'value': 1, 
      'left': {
        'value': '2L', 
        'left': {'value': '3L', 'left': None, 'right': None}, 
        'right': {'value': '3R', 'left': None, 'right': None}
        }, 
      'right': {
        'value': '2R', 
        'left': {'value': '3L', 'left': None, 'right': None}, 
        'right': {'value': '3R', 'left': None, 'right': None}
        }
      }


printNode(reverseNode(n))