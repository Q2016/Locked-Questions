Question:
You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 
Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".


 
 
 
 
Solution: DFS + Set (reminds of directory construction problem)


class Solution(object):
    def numTilePossibilities(self, tiles):

        res = set()
        
        def dfs(path, t):
            if path:
                res.add(path)
            for i in range(len(t)):
                dfs(path+t[i], t[:i] + t[i+1:])
                
        dfs('', tiles)
        return len(res)
