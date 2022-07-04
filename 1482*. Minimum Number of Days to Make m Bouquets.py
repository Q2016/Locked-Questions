Question:
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.    

    
    
    
    
    
    
    

    
    
Solution: BST
    
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/769703/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.    
    
def minDays(bloomDay: List[int], m: int, k: int) -> int:
    def feasible(days) -> bool:
        bonquets, flowers = 0, 0
        for bloom in bloomDay:
            if bloom > days:
                flowers = 0
            else:
                bonquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bonquets >= m

    if len(bloomDay) < m * k:
        return -1
    left, right = 1, max(bloomDay)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left
        return left;

Questions in this link provided for BST:
278. First Bad Version [Easy]
69. Sqrt(x) [Easy]
35. Search Insert Position [Easy]
1011. Capacity To Ship Packages Within D Days [Medium]
410. Split Array Largest Sum [Hard]
875. Koko Eating Bananas [Medium]
1482. Minimum Number of Days to Make m Bouquets [Medium]
668. Kth Smallest Number in Multiplication Table [Hard]
719. Find K-th Smallest Pair Distance [Hard]
1201. Ugly Number III [Medium]
1283. Find the Smallest Divisor Given a Threshold [Medium]


