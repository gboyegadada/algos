class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = len(s)-1
        o = l % 2 # 1 or 0
        m = (l // 2) + o
        p = ''
        for i in range(l+1):
            b = i if i < m else l-i
            
            if (b+1+b) < len(p): break
            
            _p = self.isPalindromic(s[i-b:i+b+1])
            if len(_p) > len(p): p = _p

            print('Palindrom:', p, ', i:', i, ', b:', b, ', s:', s[i-b:i+b+1])
        
        
        return p
        
    def isPalindromic(self, s: str) -> str:
        o = len(s) % 2 # 1 or 0
        m = (len(s) // 2) + o
        p =''
        
        
        for i in range(m+1-o, 0, -1):
            a, b = s[m-i-o:m-o], s[m:m+i]
            print('Check a / b:', a, b)
            
            if a == b:
                p = s[m-i-o:m] + s[m:m+i]
                break
                
        
        return p