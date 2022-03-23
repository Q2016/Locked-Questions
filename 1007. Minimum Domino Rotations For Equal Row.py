Question:
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
If it cannot be done, return -1.











Solution: hash frequency

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        
        l=len(tops)
        
        top=Counter(tops)
        bottom=Counter(bottoms)
        
        top_max=0
        for counter in [top,bottom]:
            top_max=max(top_max, sorted(counter.values())[::-1][0])
        

        return l-top_max
