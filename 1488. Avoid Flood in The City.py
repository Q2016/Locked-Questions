Question:
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, 
the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. 
Your goal is to avoid the flood in any lake. Given an integer array rains where:
rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where: ans.length == rains.length and ans[i] == -1 if rains[i] > 0. ans[i] is the lake you choose to dry 
in the ith day if rains[i] == 0. Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry 
an empty lake, nothing changes. (see example 4)

Example 1:
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.   











Solution: Greedy and Heap
    
start by getting all the days that each river is rained on, in chronological order.
then, go through each day. if a lake is rained on during a day, we get the next day that that river is going to be 
rained on in the future. we put this day in our "closest" minheap so that the next time we have a dry day, we can just pop 
from the minheap and fill up the lake that will be re-rained on nearest in the future.    



class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        seen = set()
        closest = []
        locs = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []
        for lake in rains:
            if lake in seen:
                return []
            if not lake:
                # get closest that's already seen
                if not closest:
                    # there's nothing filled that will be filled again later
                    ret.append(1) 
                    continue
                nxt = heapq.heappop(closest)
                ret.append(rains[nxt])
                seen.remove(rains[nxt])
            else:
                seen.add(lake)
                l = locs[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                ret.append(-1)
        return ret
