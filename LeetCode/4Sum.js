/**
 * LeetCode 18. 4Sum
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
const fourSum = (nums, target) => {
    let results = []
    nums.sort((a, b) => a - b)
    
    for (let i=0; i < nums.length-2; i++) {
    if (i > 0 && nums[i] === nums[i-1]) continue
      // :Three Sum
      let threeSumTarget = target - nums[i] // target === 4 sum target
      let j = i+1, k = nums.length-1
      while (j < k) {
        if (j > i+1 && nums[j] === nums[j-1]) {
          j++
          continue
        }

        // : Two Sum
        let twoSumTarget = threeSumTarget - nums[j]
        let k = j+1, l = nums.length-1
        while (k < l) {
          if (k > j+1 && nums[k] === nums[k-1]) {
            k++
            continue
          }
    
          let s2 = nums[k] + nums[l]
          if (s2 === twoSumTarget) {
            results.push([nums[i], nums[j], nums[k], nums[l]])
          }
    
          if (s2 <= twoSumTarget) k++
    
          if (s2 >= twoSumTarget) l--
        }
        
        j++
      }
    }
    
    return results
  }