class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        
        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            
            if i>=len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0,[],0)
        
        return res
      
 or:     
      
 class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
