/**
 * LeetCode 3. Longest Substring Without Repeating Characters
 * 
 * Runtime: 96 ms
 * Memory Usage: 40.5 MB
 * 
 * [ "dvdf" "abcabcbb" "bbbbb" "pwwkew" "" ]
 * 
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let current = ''
  let a = 0

  // i: substring start, j: substring end
  
  for (let i=0; i < s.length; i++) {
      let ch = s[i]
      let j = current.indexOf(ch)
      
      if (j > -1) {
          a = Math.max(a, current.length)
          current = current.substr(j+1) + ch
      }
      
      else current += ch
  }
  
  return Math.max([a, current.length])
};
