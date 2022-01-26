Question: Dont understand the question
    
    
    
    
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


greedy and heap



Variables:

dic stores the raining day for each lake in ascending order.
to_empty is a Min-heap and records the lakes that are full and sorted in urgency order. Notably, lake i has the highest urgency means that lake i is currently full and will be rained in the most recent future among all other full lakes.
full is a HashSet used to record the full lakes for efficient queries. lake in full could be replaced by lake in to_empty yet the time complexity is O(1) vs. O(n).
Logics:
We dry lakes in the order of urgency - Greedy.
Iterating through days, when day i is raining on lake lake, if lake is already full, simply return []; else, push the next raining day for lake to to_empty to queue it for drying.
When day i is sunny, dry the most urgent lake referring to to_empty. Remember to remove it from full.

Python code is as follows:

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = collections.defaultdict(list)
        ret = [-1] * len(rains)
        to_empty = [] # index
        full = set([])
        for day,lake in enumerate(rains):
            dic[lake].append(day)
        
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if lake in full:
                    return []
                full.add(lake)
                dic[lake].pop(0)
                if dic[lake]:
                    heapq.heappush(to_empty,dic[lake][0])
            else:
                if to_empty:
                    ret[i] = rains[heapq.heappop(to_empty)]
                    full.remove(ret[i])
                else:
                    ret[i] = 1
        return ret
Or we can get rid of full and take advantage of dic, not big difference tho.

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = collections.defaultdict(list)
        ret = [-1] * len(rains)
        to_empty = [] # index
        
        for day,lake in enumerate(rains):
            dic[lake].append(day)
        
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if dic[lake] and dic[lake][0] < i:
                    return []
                if dic[lake] and len(dic[lake])>1:
                    heapq.heappush(to_empty,dic[lake][1])
            else:
                if to_empty:
                    ret[i] = rains[heapq.heappop(to_empty)]
                    dic[ret[i]].pop(0)
                else:
                    ret[i] = 1
        return ret
