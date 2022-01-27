Question:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
could represent. Return the answer in any order. A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.
 1    2     3
     abc   def   
4     5     6
ghi  jkl   mno   
7     8     9
pqrs tuv   wxyz 
      0	
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]	
	
	
Solution: Combinations

    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]
