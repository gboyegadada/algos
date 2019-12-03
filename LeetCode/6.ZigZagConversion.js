/**
 * LeetCode 6. ZigZag Conversion
 * 
 * Runtime: 88 ms
 * Memory Usage: 38.1 MB
 * 
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
  if (numRows === 1) return s
  
  let i = 0, y = 0, dip = true
  let buffer = new Array(numRows).fill('')
  
  while (i < s.length) {
      
      buffer[y] += s[i]
      
      // (+) when we are dipping, (-) when we are not.
      y = dip ? y+1 : y-1
      
      // When we hit zero or peak.
      if (y === 0 || y === numRows-1) dip = !dip
      
      i++ // clock
  }
  
  return buffer.join('')
  
};


// @TODO: I think there is a maths pattern here somewhere but I haven't seen it yet 🤦🏽‍♂️

// P(y:0, i:0)                         I(y:0, i:6)                           N(y:0, i:12) 
// A(y:1, i:1)             L(y:1, i:5) S(y:1, i:7)              I(y:1, i:11) G(y:1, i:13)
// Y(y:2, i:2) A(y:2, i:4)             H(y:2, i:8) R(y:2, i:10)
// P(y:3, i:3)                         I(y:3, i:9)

// P(y:0, i:0) 
// A(y:1, i:1)
// Y(y:2, i:2)
// P(y:3, i:3)
// A(y:2, i:4) 
// L(y:1, i:5)
// I(y:0, i:6)
// S(y:1, i:7)
// H(y:2, i:8)
// I(y:3, i:9)
// R(y:2, i:10)
// I(y:1, i:11)
// N(y:0, i:12)
// G(y:1, i:13)

// P(y:0, i:0)       0 ------------------ 3
// I(y:0, i:6)       1
// N(y:0, i:12)      2

// A(y:1, i:1)       3 ------------------ 5
// L(y:1, i:5)       4
// S(y:1, i:7)       5
// I(y:1, i:11)      6
// G(y:1, i:13)      7

// Y(y:2, i:2)       8 ------------------- 4
// A(y:2, i:4)       9
// H(y:2, i:8)       10
// R(y:2, i:10)      11

// P(y:3, i:3)       12 ------------------ 5
// I(y:3, i:9)       13

//                      ------------------ 3