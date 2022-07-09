Question:
Given an integer array nums and an integer k, return the k most frequent elements. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]    

    
    
    
    
    
    
    
    
Heapify in python takes O(N), each pop() takes O(logn), then popping k elemnts takes O(klogn)    
    
Solution:   Not Heap, it takes O(klogn), we use Bucket sort O(n)  

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
        

Bucket sort:
    https://www.youtube.com/watch?v=YPTqKIgVk-k
        
        
class Solution:
    def topKFrequent(self, nums, k):
        count={}
        freq=[[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n]=1+count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
            
        res=[]
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        
Time O(n)        
        
