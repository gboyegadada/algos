/**
 * LeetCode 1. Two Sum
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let visited = new Map()
  
  for (let i=0; i < nums.length; i++) {
      const k = visited.get(nums[i])
      if (k != undefined) return [k, i]
      
      visited.set(target - nums[i], i)
  }
  
  return []
};