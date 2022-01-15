Solution:
  https://leetcode.com/problems/permutation-in-string/discuss/102594/Python-Simple-with-Explanation


This problem has many solutions but only sliding window passes all the tests

Intuition:

For each window representing a substring of s2 of length len(s1), we want to check if the count of the window is equal to the count of s1. Here, the count of a string is the list of: [the number of a's it has, the number of b's,... , the number of z's.]

We can maintain the window by deleting the value of s2[i - len(s1)] when it gets larger than len(s1). After, we only need to check if it is equal to the target. Working with list values of [0, 1,..., 25] instead of 'a'-'z' makes it easier to count later.

def checkInclusion(self, s1, s2):
    A = [ord(x) - ord('a') for x in s1]
    B = [ord(x) - ord('a') for x in s2]
    
    target = [0] * 26
    for x in A:
        target[x] += 1
    
    window = [0] * 26
    for i, x in enumerate(B):
        window[x] += 1
        if i >= len(A):
            window[B[i - len(A)]] -= 1
        if window == target:
            return True
    return False
