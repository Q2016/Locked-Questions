Question:
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, 
return the shortest distance between the given index i and the target color c. If there is no solution return -1.

Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).







  
Solution: Hash map
  
Build a mapping between color and its indices. Then for each query, do a binary search to find which 
color index is the nearest one to the query target position.


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        mapping = defaultdict(list)   
        for i, color in enumerate(colors):
            mapping[color].append(i)            
        results = []
     
        for query in queries:
            position = query[0]
            color = query[1]

            if color not in mapping:
                results.append(-1)
                continue
                
            index_list = mapping[color]
            insert = bisect.bisect_left(index_list, position)
           
            left_nearest = abs(index_list[max(insert - 1, 0)] - position)
            right_nearest = abs(index_list[min(insert, len(index_list) - 1)] - position)
            
            results.append(min(left_nearest, right_nearest))   
        return results
      
Time Complexity: O(Qlog(N) + N).
Space Complexity: O(N).
where Q is the length of queries and N is the length of colors.
