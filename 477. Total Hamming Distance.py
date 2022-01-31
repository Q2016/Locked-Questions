Question:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.

Example 1:
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6. 

Solution :
For each "column" or bit position, once you count the number of set bits you can figure out the number of pairs that will 
contribute to the count using combination logic. Consider you have 10 numbers and only one of them is a 1 the rest are zeros. 
How many (1, 0) pairs can you make? Clearly you can make 9, pair the 1 with each of the other 9 zeros. If you have 2 ones, 
you can pair each of those with the other 8 zeros giving 2*8 = 16. Keep going and you see that you can pair each 1 with each 
zero so the number of pairs is just the number of 1's times the number of 0's.
    
    def totalHammingDistance(nums) :
        count = 0
        # iterate thru "column" or bit position
        for i in range(32):
        
            mask = 1 << i
            countOnes = 0
            countZeros = 0
            for x in nums:
                if ((x & mask) != 0): 
                    countOnes++
                else :
                    countZeros++
            count += countOnes * countZeros
        return count
    
This would be an O(32 * n) solution which is an O(n) solution, no space used.
