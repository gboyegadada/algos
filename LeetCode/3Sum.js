/**
 * LeetCode 15. 3Sum
 * 
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let results = []
    nums.sort((a, b) => a - b)
      
    for (let i=0; i < nums.length-2; i++) {
      if (i > 0 && nums[i] === nums[i-1]) continue
        
      let twoSumTarget = 0 - nums[i] // 0 === three sum target
      let j = i+1, k = nums.length-1
      while (j < k) {
          if (j > i+1 && nums[j] === nums[j-1]) {
              j++
              continue
          }
  
          let s = nums[j] + nums[k]
  
          if (s === twoSumTarget) {
              results.push([nums[i], nums[j], nums[k]])
          }
  
          if (s <= twoSumTarget) j++
  
          if (s >= twoSumTarget) k--
      }
    }
    
    return results
  };