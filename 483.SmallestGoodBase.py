# -*- coding: utf-8 -*-
'''
483. Smallest Good Base

Runtime: 28 ms
Memory Usage: 12.7 MB
'''
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        max_int = 10**18
        max_expo = 2
        
        while True:
            base = math.floor(num ** (1/max_expo))
            
            if base == 1:
                break
                
            s = 0
            for p in range(0, max_expo+1):
                s = s + base**p 
                
            if base < max_int and s == num:
                return str(base)
            
            max_expo += 1
        
        return str(num-1)