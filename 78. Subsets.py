Question:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]    

    
Solution:
Algorithm

We define a backtrack function named backtrack(first, curr) which takes the index of first element to add and a current combination as arguments.
If the current combination is done, we add the combination to the final output.
Otherwise, we iterate over the indexes i from first to the length of the entire sequence n.
Add integer nums[i] into the current combination curr.
Proceed to add more integers into the combination : backtrack(i + 1, curr).
Backtrack by removing nums[i] from curr.    

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
