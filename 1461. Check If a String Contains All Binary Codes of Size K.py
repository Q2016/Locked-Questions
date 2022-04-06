Question:
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.  


    
    
    
    
    
    
    
    
    
    
Solution: Set

We just need to check every substring with length k until we get all the possible binary codes. 
Since there are two possible char for each place: 0 or 1, there will be 2^k possible binary code.
We can continue until we count up to 2^k. We will return false if did not get 2^k counts after iteration. 
To prevent repeated counting, a set can be used to store the result we previously counted.
Note that 1 << k is the same as 2^k, and we use the previous one here.

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k # 2^k
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
      
      
Complexity Analysis:
Time complexity: O(NK). We need to iterate the string, and use O(K) to calculate the hash of each substring.
Space complexity: O(NK). There are at most N strings with length K in the set. 
