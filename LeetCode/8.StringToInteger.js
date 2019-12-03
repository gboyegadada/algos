/**
 * String to Integer (atoi)
 * 
 * Runtime: 96 ms
 * Memory Usage: 36.6 MB
 * 
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
  const ref = '0123456789'
  str = str.trim()
  
  if (str === '' || (str[0] !== '-' && str[0] !== '+' && ref.indexOf(str[0]) === -1)) return 0
  
  let end = (str[0] === '-' || str[0] === '+') ? 1 : 0
  
  while (end < str.length && ref.indexOf(str[end]) !== -1) end++
  
  const n = +str.substr(0, end)
  
  if (!Number.isInteger(n)) return 0
  
  return (n < -2147483648) ? -2147483648 : (n >= 2147483647) ? 2147483647 : n
};

/**
 * String to Integer (atoi)
 * 
 * Runtime: 80 ms
 * Memory Usage: 35.9 MB
 * 
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
  str = str.match(/^\s*([-+]?\d+)/)
  if (!str) return 0
  
  const n = +str[1]
  
  if (!Number.isInteger(n)) return 0
  
  return (n < -2147483648) ? -2147483648 : (n >= 2147483647) ? 2147483647 : n
};