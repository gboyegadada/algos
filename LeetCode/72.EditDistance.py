# -*- coding: utf-8 -*-
'''
72. Edit Distance

Runtime: 232 ms
Memory Usage: 16.1 MB
'''
class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    '''
     Operations:
     __________________
    | replace | remove |
    |_________|________|
    | insert  |        |
    |_________|________|

    This video helped: 
        
    https://www.youtube.com/watch?v=MiqoA-yF-0M&t=217s

    ''' 
    if word1 == word2:
        return 0
        
    lx, ly = len(word1)+1, len(word2)+1

    m = [[0]*lx for _ in range(ly)]
    
    for x in range(lx):
      for y in range(ly):
        if x == 0 and y == 0:
          '''
          1. no op: word1[0:0] against word2[0:0]
          '''
          m[y][x] = 0
          
        elif x == 0 and y > 0:
          '''
          2. inserts: word1[0:0] against word2[:]
          '''
          m[y][x] = y
          
        elif y == 0 and x > 0:
          '''
          3. deletes:  word1[:] against word2[0:0]
          '''
          m[y][x] = x
           
        elif word1[x - 1] == word2[y - 1]: 
          '''
          4. no op: "stri(n)f" ---> "stri(n)g"

          '''
          m[y][x] = m[y-1][x-1]
          
        elif word1[x-1] != word2[y-1]: 
          '''
          5. replace: "strin(f)" ---> "strin(g)"

          '''
          m[y][x] = 1 + min(m[y-1][x-1], m[y][x-1], m[y-1][x])
          
    
    return m[y][x]
    