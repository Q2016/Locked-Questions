Question:
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
English character. You can perform this operation at most k times. Return the length of the longest substring containing 
the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2, Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.    
    
    
    
    
    
    
    
    
    
    
Solution: Sliding window 

    
There's no edge case for this question. The initial step is to extend the window to its limit, that is, the longest we can get to 
with maximum number of modifications. Until then the variable start will remain at 0.
Then as end increase, the whole substring from 0 to end will violate the rule, so we need to update start accordingly (slide the window). 
We move start to the right until the whole string satisfy the constraint again. Then each time we reach such situation, we update our max length. 

    public int characterReplacement(String s, int k) {
        int len = s.length();
        int[] count = new int[26];
        int start = 0, maxCount = 0, maxLength = 0;
        for (int end = 0; end < len; end++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            while (end - start + 1 - maxCount > k) {
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
   
    
    
    def characterReplacement(self, s, k):
        counts = collections.Counter()
        start = res = 0
        # We use a window ranging from index start to end
        # We only look in characters inside this window and keep track of their counts
        # We can allow up to K chars that are not the most frequent char in our window
        for end in range(len(s)):
            # at each loop, end is shifted to the right
            counts[s[end]] += 1 # we've seen character 's[end]' one more time in the this new window
            # we shift start to the right only if we ran out of replacements
            # we ran out of replacements if (CHARS that are not the most frequent in current window) > k
            # (end - start + 1) is length of our window, because our window range is INCLUSIVE of both ends
            if end - start + 1 - counts.most_common(1)[0][1] > k:
                # since our window will be shifted, we subtract the character that we are shifting away from by 1
                # because it will no longer be in the new window
                counts[s[start]] -= 1 
                start += 1 # now shift our window
            # at each window, simply update res if our current window is larger
            res = max(res, end - start + 1)
        
        return res

