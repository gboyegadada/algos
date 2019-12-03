/**
 * 5. Longest Palindromic Substring
 * 
 * Runtime: 92 ms
 * Memory Usage: 35.8 MB
 * 
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  let sl = s.length
  if (sl <= 1) return s
    
  let i = 0, j = 0, k = 0, t, p = ''
  
  while (i < sl) {        
      
      /* ---------- ODD length palindrome ------------ */
      
      k = i+1, j = i-1, t = s[i] 
      
      while (j >= 0 && k <= sl && s[j] === s[k]) {
              j--
              k++
      }
      t = s.slice(j+1, k)
              
      if (t.length > p.length) p = t
      
  
      /* ---------- EVEN length palindrome ------------ */
      
      k = i+1, j = i, t = ''
      
      while (j >= 0 && k <= sl && s[j] === s[k]) {
              j--
              k++
      }
      t = s.slice(j+1, k)
              
      if (t.length > p.length) p = t
      
      
      i++
  }
  
  return p
};


/**
 * 5. Longest Palindromic Substring
 * 
 * Runtime: 152 ms
 * Memory Usage: 42 MB
 * 
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
  let sl = s.length
  if (sl <= 1) return s
    
  let i = 0, j = 0, k = 0, t, p = ''
  
  while (i < sl) {        
      
      /* ---------- ODD length palindrome ------------ */
      
      k = i+1, j = i-1, t = s[i] 
      
      while (j >= 0 && k <= sl && s[j] === s[k]) {
              t = s[j] + t + s[k]
              j--
              k++
      }
              
      if (t.length > p.length) p = t
      
  
      /* ---------- EVEN length palindrome ------------ */
      
      k = i+1, j = i, t = ''
      
      while (j >= 0 && k <= sl && s[j] === s[k]) {
              t = s[j] + t + s[k]
              j--
              k++
      }
              
      if (t.length > p.length) p = t
      
      
      i++
  }
  
  return p
};


/* ----------------------- Test input ---------------------------- */ 
// "sooos"
// "babad"
// "cbbd"
// "babadcbbdreviverdeifiedkayakredividerjhytsdbbb"
// "a"
// ""
// "ac"
// "ccc"
// "aaaa"
// "aaauaaababadccc"
// "aaaabaaa"
// "tattarrattat"
// "azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"
// "tfekavrnnptlawqponffseumswvdtjhrndkkjppgiajjhklqpskuubeyofqwubiiduoylurzlorvnfcibxcjjzvlzfvsvwknjkzwthxxrowidmyudbtquktmyunoltklkdvzplxnpkoiikfijgulbxfxhaxnldvwmzpgaiumnvpdirlrutsqenwtihptnhghobrmmzcsrhqgdgzrvvitzgsolsxjxfeencvpnltxeetmtzlwnhlvgtbhkicivylfjhhfqteyxewmnewhmsnfdyneqoywgsgptwdlzbraksgajciebdchindegdfmayvfkwwkkfyxqjcv"

