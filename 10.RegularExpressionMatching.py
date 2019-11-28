# -*- coding: utf-8 -*-
'''
10. Regular Expression Matching

Runtime: 32 ms
Memory Usage: 12.9 MB
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp, memo = len(s), len(p), {}
        
        def m(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j >= lenp: 
                    ans = i >= lens
                    
                else:
                    first_match = i < lens and p[j] in {s[i], '.'}

                    if j+1 < lenp and p[j+1] == '*':
                        ans = m(i, j+2) or first_match and m(i+1, j)

                    else:
                        ans = first_match and m(i+1, j+1)
                    
                memo[i, j] = ans
            
            return memo[i, j]
            
        return m(0, 0)
        
        



# ----------------------- ☠ FAILED ATTEMPTS ☠ -------------------------------- #

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, k, m, tmp, mm = 0, 0, 0, ['']*len(p), p.replace('*', ''), ''
        
        least = 0
        
        while i < len(p):
            if (i>0): print((m, j, p[i-1], p[i], {'i': i, 'l': least}))
                
            if j == len(s) and j == 1:
                break
                #i += 1
                #continue
                
            if j < len(s) and p[i-1] == '*' and s[j] == s[j-1]:
                m[k>0 and k-1 or k] += s[j]
                j += 1
                i += 1
                
                least += 1
                
                continue
                
            elif (j < len(s) and s[j] == p[i] or p[i] == '.'):
                m[k] += s[j]
                mm = s[j]
                j += 1
                k += 1
                
                least += 1
                
                if j==len(s): 
                    i += 1
                    break
                
            elif p[i] == '*' and (p[i-1] == mm or p[i-1] == '.'):
                while j < len(s)-(len(tmp)-i) and (s[j] == mm or p[i-1] == '.'):
                    m[k-1] += s[j]
                    j += 1
                    
                    least += 1
            i += 1
                
        if j < len(s) and p[i-1] == '*' and s[j] == s[j-1]:
            m[k] += s[j]
            least += 1
            
        while i < len(p):
            if i+1 < len(p) and p[i] != '*' and p[i+1] == '*':
                i += 2
                
            elif p[i] != '*':
                i += 1
                least += 1
                
            else: i += 1
                
            
        print((m, j, p[i-1], '', least))
        print({'m': m, 'ms': "".join(m), 's': s, 'lens': len(s), 'i': i, 'j': j, 'least': least})
            
        return "".join(m) == s and len(s) == least

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, k, m, tmp, mm = 0, 0, 0, ['']*len(p), p.replace('*', ''), ''
        
        least, ast = 0, ''
        
        while i < len(p):
            if (i>0): print((m, j, p[i-1], p[i], {'i': i, 'l': least}))
                
            if j == len(s) and j == 1:
                i += 1
                break
                
            if j < len(s) and p[i-1] == '*' and s[j] == s[j-1]:
                m[k>0 and k-1 or k] += s[j]
                j += 1
                i += 1
                
                least += 1
                
                continue
                
            elif j < len(s) and (s[j] == p[i] or p[i] == '.'):
                m[k] += s[j]
                mm = s[j]
                j += 1
                k += 1
                
                if ast != p[i]: least += 1
                
                if j==len(s): 
                    i += 1
                    break
                
            elif p[i] == '*' and (p[i-1] == mm or p[i-1] == '.'):
                ast = p[i-1]
                while j < len(s)-(len(tmp)-i) and (s[j] == mm or p[i-1] == '.'):
                    m[k>0 and k-1 or k] += s[j]
                    j += 1
                    least += 1
                    
            i += 1
                
        if j < len(s) and p[i-1] == '*' and s[j] == s[j-1]:
            m[k] += s[j]
            least += 1
            
        while i < len(p):
            if i+1 < len(p) and p[i] != '*' and p[i+1] == '*':
                i += 2
                
            elif p[i] != '*':
                i += 1
                least += 1
                
            elif p[i] != '*':
                i += 1
                least += 1
                
            else: i += 1
                
            
        print((m, j, p[i-1], '', least))
        print({'m': m, 'ms': "".join(m), 's': s, 'lens': len(s), 'i': i, 'j': j, 'least': least})
            
        return "".join(m) == s and len(s) >= least


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j, k, m, tmp, mm = 0, 0, 0, ['']*len(p), p.replace('*', ''), ''
        
        least, ast = 0, ''
        
        while i < len(p):
            if (i>0): print((m, j, p[i-1], p[i], {'i': i, 'l': least}))
                
            if j == len(s) and j == 1:
                if p[i] == '*': ast = p[i-1]
                i += 1
                break
                
            if j < len(s) and p[i-1] == '*' and s[j] == s[j-1]:
                m[k>0 and k-1 or k] += s[j]
                j += 1
                i += 1
                
                least += 1
                
                continue
                
            elif j < len(s) and (s[j] == p[i] or p[i] == '.'):
                m[k] += s[j]
                mm = s[j]
                j += 1
                k += 1
                
                if ast != p[i]: least += 1
                    
                if i+1 < len(p) and p[i+1] == '*': ast = p[i]
                
                if j==len(s): 
                    i += 1
                    break
                
            elif p[i] == '*' and (p[i-1] == mm or p[i-1] == '.'):
                ast = p[i-1]
                while j < len(s)-(len(tmp)-i) and (s[j] == mm or p[i-1] == '.'):
                    m[k>0 and k-1 or k] += s[j]
                    j += 1
                    least += 1
                    
            i += 1
            
        print('DEBUG', 'A', i)
                
        if j < len(s) and p[i-1] == '*' and s[j] == s[j-1]:
            m[k] += s[j]
            least += 1
            
        print('DEBUG', 'B', i)
            
        while i < len(p):
            if i+1 < len(p) and p[i] != '*' and p[i+1] == '*':
                ast = p[i]
                i += 2
                continue
                
            elif p[i] != '*' and ast != p[i]:
                least += 1
                
            i += 1
                
            
        print((m, j, p[i-1], '', least))
        print({'m': m, 'ms': "".join(m), 's': s, 'lens': len(s), 'i': i, 'j': j, 'least': least, 'ast': ast})
            
        return "".join(m) == s and len(s) >= least

# ------------------------ TEST CASES --------------------- #

''' 
"a"
".*."
"ab"
".*.."
"a"
".*..a*"
"a"
"ab*a"
"aa"
"aa"
"aaa"
"ab*a*c*a"
"bbbba"
".*a*a"
"aaa"
"aaaa"
"a"
"ab*"
"aaa"
"ab*a"
"aaa"
"a*a"
"mississippi"
"mis*is*p*."
"ab"
".*"
"aa"
"a*"
"ab"
".*c"

'''