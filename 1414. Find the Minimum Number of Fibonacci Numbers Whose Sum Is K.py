Question:
Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. 
The same Fibonacci number can be used multiple times.

Example 1:
Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.    



Solution: Greedy (The hard part is to find the complexity)
    
Apparently we need to prove that Greedy works in the interview:
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585632/JavaC%2B%2BPython-Easy-Prove    
    
    
We greedily subtract the biggest Fibonacci number x from k,
and recursive to find the result for k - x.
Then f(k) = f(k - x) + 1

(Cost of kth fibonatci is O(logk): If we use the power formula the cost is not O(1) because cost of power is like O(log n) since binary search is
involved for implementing a power function. So at each step we need one Fibo number and one search (number less than the Fibo) so:   )

Time O((logk)^2), since O(log k) Fibonacci numbers smaller than k.
Space O(logK), can be saved by tail recursion.


    def findMinFibonacciNumbers(self, k):
        if k < 2: return k
        a, b = 1, 1
        while b <= k: # finding fibo numbers upto k
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1

    
    
