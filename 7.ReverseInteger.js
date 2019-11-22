/**
 * 7. Reverse Integer
 * 
 * Runtime: 68 ms
 * Memory Usage: 36 MB
 * 
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  const numStr = x+''
  
  if (numStr[1] === '.') return -1
  
  const result = (x >= 0) 
      ? +(numStr.split('').reverse().join(''))
      : +('-' + numStr.substr(1).split('').reverse().join(''))
  
  return (result < 2147483648 && result > -2147483648) ? result : 0
};

/**
 * 7. Reverse Integer (Alt solution)
 * 
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  let r = 0
  const INT_MAX = 2**31-1
  const INT_MIN = -(2**31)
  
  while (x !== 0) {
      let pop = x % 10
      x = ~~(x / 10)
      
      if (r > INT_MAX/10 || (r === INT_MAX/10 && pop > 7)) return 0
      if (r < INT_MIN/10 || (r === INT_MIN/10 && pop > -8)) return 0
      
      r = r * 10 + pop
  }
  
  return r
};
