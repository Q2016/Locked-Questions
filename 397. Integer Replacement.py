Question:
Given a positive integer n and you can do operations as follow: If n is even, replace n with n/2. If n is odd, 
you can replace n with either n + 1 or n - 1. What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:8, Output: 3, Explanation: 8 -> 4 -> 2 -> 1

                  
                  
                  
                  
                  
                  
                  
                  
      
Solution:  (We do direct approach similar to 1342.)    
Denote f(n) the minimum number of jumps from n to 1. By definition, we have the recurrence 
f(1) = 0, f(2n) = 1 + f(n), f(2n + 1) = min(f(2n) + 1, f(2n + 2) + 1). First notice that this sequence is well defined 
because f(2n + 2) = f(n + 1) + 1, so f(2n + 1) = min(f(2n) + 1, f(n + 1) + 2). Every element is defined by some element before it.

    def integerReplacement(self, n):
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n/2, memo)
            return memo[n]
