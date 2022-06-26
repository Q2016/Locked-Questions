Question:
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:
Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:


  
  
  
  
  
  
  
Solution: BS (makes sense, you use BS to pick string)
  
https://www.youtube.com/watch?v=Tf_mD59DLf0  
  
  
function longestRepeatingSubstring(s) {
  l = 0;
  r = s.length - 1;
  while (l < r) {
    let mid = Math.floor(l + (r - l + 1) / 2);
    if (verifyLengthOfLRS(s, mid)) {
      l = mid;
    } else {
      r = mid - 1;
    }
  }
  return l;
}


function verifyLengthOfLRS(s, mid) {
  let arr = [];
  for (let i = 0; i <= s.length - mid; i++) {
    let j = i + mid - 1;
    let sub = s.substring(i, j + 1);
    if (arr.includes(sub)) {
      return true;
    }
    arr.push(sub);
  }
  return false;
}
}
