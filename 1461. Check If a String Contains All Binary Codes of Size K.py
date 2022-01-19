Approach 1: Set
  
Recall (part of) the problem:

Return True if every binary code of length k is a substring of s. Otherwise, return False.

We just need to check every substring with length k until we get all the possible binary codes. 
Since there are two possible char for each place: 0 or 1, there will be 2^k possible binary code.

We can continue until we count up to 2^k. 
We will return false if did not get 2^k counts after iteration. To prevent repeated counting, a 
set can be used to store the result we previously counted.

Note that 1 << k is the same as 2^k, and we use the previous one here.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False
      
      
 class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k
      
      
