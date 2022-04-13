Question:
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order. You must write an algorithm that runs 
in O(n) time and uses O(1) extra space.  For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].


Solution:
I just sort the numbers 1 to n using my custom comparison. To compare two numbers, I "left-shift" them both before comparing them. 
For example if n = 49999, then I left-shift numbers so they're five digits. That is, 42 becomes 42000 and 123 becomes 12300. 
In case of ties, e.g., 420 also becoming 42000, the stability of sorted keeps them in order.

def lexicalOrder(self, n):
    top = 1
    while top * 10 <= n:
        top *= 10
    def mycmp(a, b, top=top):
        while a < top: a *= 10
        while b < top: b *= 10
        return -1 if a < b else b < a
    return sorted(xrange(1, n+1), mycmp)
            
Complexity
I think Time complexity and space complexity are both O(n) (at least if sort does what I think it does, I'll check some more), and the space 
complexity has a low hidden factor.

The time and memory limits for Python for this problem are pretty low, requiring a fairly efficient solution. On LeetCode, Python ints are 64 bits, 
so embedding the left-aligned version of numbers in the numbers (solution 2) doesn't cost extra memory. Also, sorting simple ints is fast. 
Especially since the order from 1 to n is already largely sorted lexicographically, like the streak from 100 to 999 and the streak from 1000 to 9999. 
And Python's (Tim)sort can take advantage of those streaks and just merge them. If it merges "left to right" like I think it does, then it merges 
the small streaks first and only integrates the longest streaks last, which leads to overall O(n) time.
