Question:
Given a string s and an integer k, return the length of the longest substring of s such that the 
frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

    
Solution: (Divide And Conquer)

In the first pass I record counts of every character in a hashmap. In the second pass I locate the first character that appear 
less than k times in the string. This character is definitely not included in the result, and that separates the string into two parts.
keep doing this recursively and the maximum of the left/right part is the answer.

    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)
        

