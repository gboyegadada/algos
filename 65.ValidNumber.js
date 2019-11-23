/**
 * 65. Valid Number
 * 
 * Runtime: 92 ms
 * Memory Usage: 36.2 MB
 * 
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
  return /^[-+]?(\d+(\.\d*)?|\.\d+)(e[-+]?\d+)?$/.test(s.trim())
};

/* ----------- Test Cases ------------ */

// "1."
// ".1"
// "0"
// " 0.1 "
// "abc"
// "1 a"
// "2e10"
// " -90e3   "
// " 1e"
// "e3"
// " 6e-1"
// " 99e2.5 "
// "53.5e93"
// " --6 "
// "-+3"
// "95a54e53"
