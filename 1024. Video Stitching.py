Question:
You are given a series of video clips from a sporting event that lasted time seconds. 
These video clips can be overlapping with each other and have varying lengths.
Each video clip is described by an array clips where clips[i] = [starti, endi] 
indicates that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments 
that cover the entire sporting event [0, time]. If the task is impossible, return -1.



Solution: Sort+Greedy
    
The intuitve heuristic is that we iterate clips with order by their starting time and keep 
increasing furthest ending time we can reach.

If the starting time of current clips is later than current furthest ending time, then 
stitching is not doable since none of the rest clips' starting time is earlier. Once 
furthest ending time >= T, we have finished video stitching.

And to get the minimal number of clips we need, we need to remove all unncessary clips during the scan.
Suppose we already have clips [s0, e0] and next two clips are [s1, e1] and [s2, e2]. 
If s2 <= e0, then s0 <= s1 <= s2 <= e0 and only one of two clips are needed. Thus, we use prev_end 
to store e0 and each time s <= prev_end, we don't add up cnt. Othwise, we have to add one 
more clip and update prev_end accordingly. The furthest ending time just gets updated each time as max(furthest_end, e).    

Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].    
    
    
    
    
    
    
    def videoStitching(self, clips, T):
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= T else -1
