Question:
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at 
the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.    
    
    
Solution:    
We don't need to actually generate the strings "0110..." (would be TLE error anyway)

row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
We see that, for any level N, the first half of the string is the same as the string in N-1, the next half is just complement of it. 
The total number of items in level N is 2^N. The half mark of the string is marked by [2^(N-1)]-th item. So, for any level N:

if K is in the first half, it is same as the Kth element in level N-1
if K is in the second half, it is the complement of the number in [K-2^(N-1)]-th position in level N-1
So, we run the recursion until the base condition (N=1)

class Solution(object):
    def kthGrammar(self, N, K):
        if N==1:
            if K==1:
                return 0
            else:
                return 1
            
        half=2**(N-1)
        if K<=half:
            return self.kthGrammar(N-1,K)
        else:
            res=self.kthGrammar(N-1,K-half)
            if res==0:
                return 1
            else:
                return 0    
