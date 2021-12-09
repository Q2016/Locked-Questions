# sliding window


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        n=len(fruits)
        l,r=0,0
        
        maxfruit=0
        limit=set()
        while l<=r:
            while r<n:
                
                
                if fruits[l] not in limit and len(limit)<2:
                    limit.add(fruits[l])
                    maxfruit=max(maxfruit, fruits[l])
                elif len(limit)>2:
                    l=r
                r+=1
                
        return maxfruit
