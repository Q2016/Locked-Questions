A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  
If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

Example 1:
Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

Example 2:
Input: "abcd"
Output: ["abcd"]

Note:
1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.




# Recursion
https://goodtecher.com/leetcode-1087-brace-expansion/

Explanation
The goal of the problem is to find all combination strings. Whenever we encounter a ‘{‘, 
we can build combinations from different options, after that, we go to the character after ‘}’ 
to continue building combinations. When we encounter a letter, we just go to the next character 
in the string. In the end, sort the results in alphabetically ascending order.

Python Solution
class Solution:
    def expand(self, s: str) -> List[str]:
        results = []
        
        end = len(s)
        
        self.helper(results, "", 0, s)
        
        results = sorted(results)
        
        return results
                
    def helper(self, results, combination, start, s):        
        if start == len(s):
            results.append(combination)
            return
        
        i = start
        
        if s[i] == '{':
            j = i + 1            
            
            options = []

            while s[j] != '}':
                if s[j] != ',':
                    options.append(s[j])
                j += 1
            
            for option in options:                
                self.helper(results, combination + option, j + 1, s)

        elif s[i] == '}':
            return
        
        else:                
            self.helper(results, combination + s[i], i + 1, s)
Time Complexity: O(N).
Space Complexity: O(N).
