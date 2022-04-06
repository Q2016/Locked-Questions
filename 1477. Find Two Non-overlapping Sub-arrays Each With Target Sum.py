Question:
You are given an array of integers arr and an integer target. You have to find two non-overlapping sub-arrays 
of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum
of the lengths of the two sub-arrays is minimum. Return the minimum sum of the lengths of the two required 
sub-arrays, or return -1 if you cannot find such two sub-arrays.    

Example 1:
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2


    
Solution: O(N) Time, Two Pass Solution using HashMap

Concept: First traverse through the array once and store the (key,value) pair as (sum(arr[0:i+1]),i) for 0<=i<size of arr. Put, (0,-1) 
in hashmap as default. Now traverse through the array again, and for every i, find the minimum value of length of sub-array on the left or 
starting with i whose value is equal to target. Find another sub-array starting with i+1, whose sum is target. Update the result with the 
minimum value of the sum of both the sub-array. This is possible because all values are positive and the value of sum is strictly increasing.

C++:
class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        HashMap<Integer,Integer> hmap=new HashMap<>();
        int sum=0,lsize=Integer.MAX_VALUE,result=Integer.MAX_VALUE;
        hmap.put(0,-1);
        for(int i=0;i<arr.length;i++){
            sum+=arr[i];
            hmap.put(sum,i); # stores key as sum upto index i, and value as i.
        }
        sum=0;
        for(int i=0;i<arr.length;i++){
            sum+=arr[i];
            if(hmap.get(sum-target)!=null){
                # stores minimum length of sub-array ending with index<= i with sum target. This ensures non- overlapping property.
                lsize=Math.min(lsize,i-hmap.get(sum-target));      
            }
	    #hmap.get(sum+target) searches for any sub-array starting with index i+1 with sum target.
            if(hmap.get(sum+target)!=null&&lsize<Integer.MAX_VALUE){
                result=Math.min(result,hmap.get(sum+target)-i+lsize); # updates the result only if both left and right sub-array exists.
            }
        }
        return result==Integer.MAX_VALUE?-1:result;
    }
}

Python:
class Solution: 
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        
        # 1st scan, getting better result (smaller length) as we scan
        left = [inf] * n
        s = 0 # pre sum
        shortest = inf
        m = {0: -1}  # sum -> index
        for i in range(n):
            s += arr[i]
            if s - target in m:
                shortest = min(shortest, i - m[s - target])
            left[i] = shortest
            m[s] = i
            
        # 2nd scan, getting better result (smaller length) as we scan
        right = [inf] * n
        s = 0 # pre sum (from right to left)
        shortest = inf
        m = {0: n}
        for i in range(n)[::-1]:
            s += arr[i]
            if s - target in m:
                shortest = min(shortest, abs(i - m[s - target]) )
            right[i] = shortest
            m[s] = i
        
        # combine
        res = inf
        for i in range(1 , n):
            # Non-overlapping subarrays.
            # Check adj results because during each scan,
            # the length will only get smaller if possible
            if left[i - 1] != inf and right[i] != inf:
                res = min(res, left[i - 1] + right[i])
        
        return res if res != inf else -1	
