# hash frequency

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        
        l=len(tops)
        
        top=Counter(tops)
        bottom=Counter(bottoms)
        
        top_max=0
        for counter in [top,bottom]:
            top_max=max(top_max, sorted(counter.values())[::-1][0])
        

        return l-top_max
