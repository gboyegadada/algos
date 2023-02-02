class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = '' # our sliding window
        m = 0 # max
        
        '''
        i: substring start index
        j: index of a repeated character in our window
        '''
        for c in s:
            
            '''
            is the current character already in our sliding window?
            '''
            j = w.find(c)
            
            if j > -1:
                m = max(len(w), m)
                w = w[j+1:] + c
                
            else:
                w += c
                
        m = max(len(w), m)
        
        return m
        