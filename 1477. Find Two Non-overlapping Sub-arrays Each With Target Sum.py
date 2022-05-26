Question:
You are given an array of integers arr and an integer target. You have to find two non-overlapping sub-arrays 
of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum
of the lengths of the two sub-arrays is minimum. Return the minimum sum of the lengths of the two required 
sub-arrays, or return -1 if you cannot find such two sub-arrays.    

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2


  







Solution: Dp
	
def minSumOfLengths(self, arr: List[int], target: int) -> int:
	n=len(arr)
	dp=[sys.maxsize]*n
	
	left=0
	ans=sys.maxsize
	running_sum=0
	cur_shortest=sys.maxsize
	
	for right, num in enumerate(arr):
		running_sum+=num
		
		while running_sum>target:
			running_sum-=arr[left]
			left+=1
		if running_sum==target:
			if left>0 and dp[left-1]<sys.maxsize:
				ans=min(ans, dp[left-1]+right-left+1)
			
			cur_shortest=min(cur_shortst, right-left+1)
			
		dp[left]=cur_shortest
	
	return ans

  
