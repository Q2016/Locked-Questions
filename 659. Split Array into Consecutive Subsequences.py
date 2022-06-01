Question:
You are given an integer array nums that is sorted in non-decreasing order. Determine if it is possible to split nums into one or 
more subsequences such that both of the following conditions are true: Each subsequence is a consecutive increasing sequence. 
All subsequences have a length of 3 or more. Return true if you can split nums according to the above conditions, or false otherwise. 

Example 1:
Input: nums = [1,2,3,3,4,5], Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3 and 3, 4, 5  

Example 2:
Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5






Solution: greedy heap 
  
  From this link: https://www.youtube.com/watch?v=hbNUEvWyiFU

 def isPossible(self, nums: List[int]) -> bool:
        end  = defaultdict(list)
    
        for num in nums:
            if num-1 not in end:
                heapq.heappush(end[num],1) 
            else:
                pre_length=heapq.heappop(end[num-1])
                
                if len(end[num-1])==0:
                    del end[num-1]
                    
                heapq.heappush(end[num],pre_length+1)
        
        if any(min(end[num])<3 for num in end):
            return False
        
        return True
