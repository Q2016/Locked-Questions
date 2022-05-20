Question:
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0. Return the minimum number of flips to make s monotone increasing.

Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.    



    
    
    
    
    
    
Solution: Similar to 122. Best Time to Buy and Sell Stock III

Approach 1: Prefix Sums

Intuition

For say a 5 digit string, the answer is either '00000', '00001', '00011', '00111', '01111', or '11111'. Let's try to calculate the cost of switching 
to that answer. The answer has two halves, a left (zero) half, and a right (one) half.
Evidently, it comes down to a question of knowing, for each candidate half: how many ones are in the left half, and how many zeros are in the right half.
We can use prefix sums. Say P[i+1] = A[0] + A[1] + ... + A[i], where A[i] = 1 if S[i] == '1', else A[i] = 0. We can calculate P in linear time.
Then if we want x zeros followed by N-x ones, there are P[x] ones in the start that must be flipped, plus (N-x) - (P[N] - P[x]) zeros that must be flipped. The last calculation comes from the fact that there are P[N] - P[x] ones in the later segment of length N-x, but we want the number of zeros.

Algorithm

For example, with S = "010110": we have P = [0, 0, 1, 1, 2, 3, 3]. Now say we want to evaluate having x=3 zeros.
There are P[3] = 1 ones in the first 3 characters, and P[6] - P[3] = 2 ones in the later N-x = 3 characters.
So, there is (N-x) - (P[N] - P[x]) = 1 zero in the later N-x characters.
We take the minimum among all candidate answers to arrive at the final answer.

class Solution(object):
    def minFlipsMonoIncr(self, S):
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in xrange(len(P)))
    

    
Complexity Analysis

Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N).    
