Question:
You are given a series of video clips from a sporting event that lasted time seconds. 
These video clips can be overlapping with each other and have varying lengths.
Each video clip is described by an array clips where clips[i] = [starti, endi] 
indicates that the ith clip started at starti and ended at endi.
We can cut these clips into segments freely.
For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments 
that cover the entire sporting event [0, time]. If the task is impossible, return -1.


Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].  





Solution: Greedy?
    
Idea: Related to Jump Game II question:
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index. Input: nums = [2,3,1,1,4], Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.		


	
Convert clips to the furthest point you can jump from each point. 
Do a jump game O(N).


    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        max_jumps = [0]*101
        for l,r in clips:
            max_jumps[l] = max(max_jumps[l], r)
            
        # it is then a jump game
		res = lo = hi = 0
        while hi < T:
            lo, hi = hi, max(max_jumps[lo:hi+1])
            if hi <= lo: return -1
            res += 1
        return res
