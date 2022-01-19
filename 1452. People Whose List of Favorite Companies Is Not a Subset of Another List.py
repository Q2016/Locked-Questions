https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/discuss/636512/Python3-Easy-Solution



Thanks to Python set library

class Solution:
    def peopleIndexes(self, A: List[List[str]]) -> List[int]:
        d = {i: set(v) for i, v in enumerate(A)}
        res = []
        for i in range(len(A)):
            subSet = True
            for j in range(len(A)):
                if i == j:
                    continue
                if not d[i] - d[j]:
                    subSet = False
                    break
            if subSet: res.append(i)         
        return res  
