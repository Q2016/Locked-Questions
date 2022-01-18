https://leetcode.com/problems/beautiful-arrangement-ii/solution/

Intuition

When k = n-1, a valid construction is [1, n, 2, n-1, 3, n-2, ....]. One way to see this is, we need 
to have a difference of n-1, which means we need 1 and n adjacent; then, we need a difference of n-2, etc.

Also, when k = 1, a valid construction is [1, 2, 3, ..., n]. So we have a construction when n-k is tiny, 
and when it is large. This leads to the idea that we can stitch together these two constructions: we can put 
[1, 2, ..., n-k-1] first so that n is effectively k+1, and then finish the construction with the first "k = n-1" method.

For example, when n = 6 and k = 3, we will construct the array as [1, 2, 3, 6, 4, 5]. This consists of two parts: 
a construction of [1, 2] and a construction of [1, 4, 2, 3] where every element had 2 added to it (i.e. [3, 6, 4, 5]).

Algorithm

As before, write [1, 2, ..., n-k-1] first. The remaining k+1 elements to be written are [n-k, n-k+1, ..., n], and 
we'll write them in alternating head and tail order.

When we are writing the ith element from the remaining k+1, every even i is going to be chosen from the head, 
and will have value n-k + i//2. Every odd ii is going to be chosen from the tail, and will have value n - i//2.


class Solution(object):
    def constructArray(self, n, k):
        ans = list(range(1, n - k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i//2)
            else:
                ans.append(n - i//2)

        return ans
