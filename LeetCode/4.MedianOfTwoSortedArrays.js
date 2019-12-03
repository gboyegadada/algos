/**
 * LeetCode 4. Median of Two Sorted Arrays (Optimized)
 * 
 * Runtime: 112 ms
 * Memory Usage: 38.8 MB
 * 
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  let i = 0
  let j = 0
  let k = 0
  
  let mid = (nums1.length + nums2.length) / 2
  let end = Math.floor(mid)
  
  let a = null, b = null
  
  while (k <= end) {
      while (i < nums1.length && k <= end && (j >= nums2.length || nums1[i] <= nums2[j])) {
          a = b 
          b = nums1[i++]
          k++
      }
      while (j < nums2.length && k <= end && (i >= nums1.length || nums2[j] <= nums1[i])) {
          a = b 
          b = nums2[j++]
          k++
      }
  }
  
  return Number.isInteger(mid) ? (a + b) / 2 : b
  
};


/**
 * LeetCode 4. Median of Two Sorted Arrays
 * 
 * Runtime: 128 ms
 * Memory Usage: 39.2 MB
 * 
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  let i = 0
  let j = 0
  let k = 0
  
  let mid = (nums1.length + nums2.length) / 2
  let end = Math.floor(mid)
  
  let m = []
  
  while (k <= end) {
      while (i < nums1.length && k <= end && (j >= nums2.length || nums1[i] <= nums2[j])) {
          m.push(nums1[i++])
          k++
      }
      while (j < nums2.length && k <= end && (i >= nums1.length || nums2[j] <= nums1[i])) {
          m.push(nums2[j++])
          k++
      }
      
      if (m.length > 2) m = m.slice(-2)  // We only need last 2
  }
  
  return Number.isInteger(mid) ? (m[m.length-1] + m[m.length-2]) / 2 : m[m.length-1]
  
};