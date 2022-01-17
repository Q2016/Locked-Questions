class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1
        
        for i in range(n if n <= 10 else 10):
            product *= choices[i]
            ans += product
            
        return ans
For the first (most left) digit, we have 9 options (no zero); for the second 
digit we used one but we can use 0 now, so 9 options; and we have 1 less option 
for each following digits. Number can not be longer than 10 digits.
