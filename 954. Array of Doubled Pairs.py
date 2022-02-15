Question:
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for 
every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:
Input: arr = [3,1,3,6]
Output: false

Solution: Greedy
If x is currently the array element with the least absolute value, it must pair with 2*x, as there does not exist any other x/2 to pair with it.
Let's try to (virtually) "write" the final reordered array.
Let's check elements in order of absolute value. When we check an element x and it isn't used, it must pair with 2*x. We will attempt to write x, 
2x - if we can't, then the answer is false. If we write everything, the answer is true.
To keep track of what we have not yet written, we will store it in a count.


class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True
