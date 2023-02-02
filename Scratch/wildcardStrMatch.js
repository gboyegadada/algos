/**
 * function setup(['say', 'car', 'cat'...])
 * 
 * function isInDict(word)
 * 
 * Zero or single wildcard in word
 * 
 * Source: https://www.youtube.com/watch?v=yju4zwKSriI
 */

let dict = new Set()

/**
 * @param {Array.<string>} input 
 */
function setup(input) {

  // O(n^2)
  input.forEach(s => {
    dict.add(s)

    // O(n)
    for (let i=0; i < s.length; i++) {
      let pattern = s.substr(0, i) + '*' + s.substr(i+1)
      dict.add(pattern)
    }
  })
}

function isInDict(word) {
  // O(1)
  return dict.has(word)
}

setup(['cat', 'say', 'boy', 'car', 'tap', 'bat'])


console.log('cat', isInDict('cat')) // true
console.log('*at', isInDict('*at')) // true
console.log('*ar', isInDict('*ar')) // true
console.log('*ab', isInDict('*ab')) // false
console.log('air', isInDict('air')) // false