# -*- coding: utf-8 -*-
'''
44. Wildcard Matching

Runtime: 688 ms
Memory Usage: 123.6 MB
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp, memo = len(s), len(p), {}
        
        def m(i: int, j: int) -> bool:
            if (i, j) not in memo:
            
                if j >= lenp: 
                    r = i >= lens

                else:
                    f = i < lens and p[j] in {s[i], '?', '*'}

                    if p[j] == '*':
                        r = m(i, j+1) or f and m(i+1, j)

                    else:
                        r = f and m(i+1, j+1)

                memo[i, j] = r
            
            return memo[i, j]
        
        return m(0, 0)