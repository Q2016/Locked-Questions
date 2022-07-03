Question:
There are several cards arranged in a row, and each card has an associated number of points. 
The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost 
card first will maximize your total score. The optimal strategy is to take the three cards on the right, 
giving a final score of 1 + 6 + 5 = 12.    
    
    










One way of thinking was to sort and keep positions

Solution: Sliding window (Cute question)

Problem Translation: Find the smallest subarray sum of length len(cardPoints) - k

https://www.youtube.com/watch?v=TsA4vbtfCvo	
	
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r =0, len(cardPoints) - k
	total=sum(cardPoints[r:])
	res=total
	
	while r<len(cardPoints):
	   total+=(cardPoints[l]-cardPoints[r])
	   res=max(res, total)
	   l+=1
	   r+=1
		
	return res



	
	
	
	
	
Another way of more intuitive way: Prefix sum

How to solve exactly?

Find cumulative sum from beginning to the current index.
Find cumulative sum from behind till the current index.
If you choose i elements from front, you will need to choose k-i elements from behind.
Sum of first i elements = cumulativeSumFromFront[i],
Sum of last (k-i) elements = cumulativeSumFromBehind[K-i].
So points obtained when choosing i elements from the front = cumulativeSumFromFront[i] + cumulativeSumFromBehind[K-i]
Repeat Step 3 for all i ranging from 0 to K.
Return the maximum value of points reached.
Hope it is easy to understand.
Let me know if there is something unclear and I can fix it.

Otherwise, please upvote if you like the solution, it would be encouraging.

Python (Python can be amazing at reducing lines of code)

class Solution(object):
    def maxScore(self, cardPoints, k):
        print 'cardPoints:', cardPoints
        print 'k:', k
        frontSum, backSum = [0], [0]
        for n in cardPoints:
            frontSum.append(frontSum[-1]+n)
            print 'frontSum:', frontSum
        for n in cardPoints[::-1]:
            backSum.append(backSum[-1]+n)
            print 'backSum:', backSum
        allCombinations = [frontSum[i]+backSum[k-i] for i in range(k+1)]
        print 'allCombinations:', allCombinations
        return max(allCombinations)


