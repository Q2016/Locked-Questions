Question:
Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. 
The same Fibonacci number can be used multiple times.

Example 1:
Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.    



Solution: Greedy
    
We greedily subtract the biggest Fibonacci number x from k,
and recursive to find the result for k - x.
Then f(k) = f(k - x) + 1

    def findMinFibonacciNumbers(self, k):
        if k < 2: return k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1

    
    
Time O((logk)^2), since O(log k) Fibonacci numbers smaller than k.
Space O(logK), can be saved by tail recursion.
    
