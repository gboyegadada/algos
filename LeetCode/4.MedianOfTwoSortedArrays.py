"""
LeetCode 4. Median of Two Sorted Arrays (Optimized)

Runtime: 96 ms
Memory Usage: 14.6 MB

@param {number[]} nums1
@param {number[]} nums2
@return {number}
 """

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        lx = l1 + l2
        
        if (lx % 2) == 0: # even
            i = int((lx / 2) - 1)
            m, n = i, i+1
        else: # odd
            i = int(-(lx // -2) - 1) # floor division
            m, n = i, None
            
        # print('Mid:', m, n, l1, l2)
        
        z, c = [], 0
        i = 0
        j = 0
        
        while c <= m+1 and (i < l1 or j < l2):
            c += 1
            
            if i < l1 and j >= l2:
                z.append(nums1[i])
                i += 1
            elif j < l2 and i >= l1:
                z.append(nums2[j])
                j += 1
            elif nums1[i] > nums2[j]:
                z.append(nums2[j])
                j += 1
            else:
                z.append(nums1[i])
                i += 1
        
        # print('Z:', z, 'c:', c)
        
        return z[m] if n is None else (z[m] + z[n]) / 2
                
                
            
        