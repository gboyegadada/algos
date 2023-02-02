"""
My solution: works but times out when submitted :(
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        a, b, c = set(), set(), set()
        
        for i in range(n):
            for j in range(n):
                # a <--- left side
                a.add((i, j, nums1[i] + nums2[j]))
                
                # b ---> right side
                b.add((i, j, nums3[i] + nums4[j]))
                
                
        for x in a:
            for y in b:
                # a / b
                s = x[2] + y[2]
                if s == 0:
                    c.add((x[0:2] + y[0:2], s))
                
        print('Lenths:', c)
        
        return len(c)


"""
Correct solution is not mine and I don't fully understand it yet.

Assignment: find explainer for solution tomorrow.
"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = {}
        
        for a in nums1:
            for b in nums2:
                m[a + b] = m.get(a + b, 0) + 1
                
        count = 0    
        for x in nums3:
            for y in nums4:
                count += m.get(-x-y, 0)
                
        print('Lenths:', count)
        
        return count
        