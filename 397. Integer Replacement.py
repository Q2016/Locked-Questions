Question:
# Given a positive integer n and you can do operations as follow: If n is even, replace n with n/2. If n is odd, 
you can replace n with either n + 1 or n - 1. What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:8, Output: 3, Explanation: 8 -> 4 -> 2 -> 1

      
Solution:      
Denote f(n) the minimum number of jumps from n to 1. By definition, we have the recurrence 
f(1) = 0, f(2n) = 1 + f(n), f(2n + 1) = min(f(2n) + 1, f(2n + 2) + 1). First notice that this sequence is well defined 
because f(2n + 2) = f(n + 1) + 1, so f(2n + 1) = min(f(2n) + 1, f(n + 1) + 2). Every element is defined by some element before it.
We want to show (*):
If n % 4 = 3 and n != 3, then f(n) = f(n + 1) + 1.
If n % 4 = 1 or n = 3, then f(n) = f(n - 1) + 1.
This gives us an O(log n) time, O(1) space solution.      
# Iterative solution.
    def integerReplacement(self, n):

        result = 0
        while n != 1:
            b = n & 3
            if n == 3:
                n -= 1
            elif b == 3:
                n += 1
            elif b == 1:
                n -= 1
            else:
                n /= 2
            result += 1 
        return result
      
# Time:  O(logn)
# Space: O(1)            


# Recursive solution.
    def integerReplacement(self, n):

        if n < 4:
            return [0, 0, 1, 2][n]
        if n % 4 in (0, 2):
            return self.integerReplacement(n / 2) + 1
        elif n % 4 == 1:
            return self.integerReplacement((n - 1) / 4) + 3
        else:
            return self.integerReplacement((n + 1) / 4) + 3

# Time:  O(logn)
# Space: O(logn)
          
