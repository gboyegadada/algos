# -*- coding: utf-8 -*-
'''
1143. Longest Common Subsequence

Runtime: 456 ms
Memory Usage: 20.5 MB
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        text1: cols (x)
        text2: rows (y)
        
            ''  a  b  c
        -------------------
        ''   0  0  0  0
        -------------------
        a   0  1  1  1
        -------------------
        b   0  1  2  2
        -------------------
        c   0  1  2  3
        -------------------
        d   0  1  2  3
          
          
        This video helped: 
        
        https://www.youtube.com/watch?v=ASoaQq66foQ
         
        '''
        
        lx, ly = len(text1)+1, len(text2)+1
        
        m = [[0]*lx for _ in range(ly)]
        
        for x in range(lx):
            for y in range(ly):
                if x == 0 or y == 0:
                    m[y][x] = 0
                    
                elif text1[x-1] == text2[y-1]:
                    m[y][x] = 1 + m[y-1][x-1]
                    
                else:
                    m[y][x] = max(m[y-1][x], m[y][x-1])
                    
        return m[y][x]
            