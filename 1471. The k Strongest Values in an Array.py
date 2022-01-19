
https://leetcode.com/problems/the-k-strongest-values-in-an-array/discuss/674566/Python3-straightforward-2-lines-with-custom-sort


get median by sorting and getting the (n-1)/2 th element
use lambda to do custom sort. since we need maximum, take negative of difference. if difference is equal, we just get the larger value element
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = sorted(arr)[(len(arr) - 1) // 2]
        return sorted(arr, key = lambda x: (-abs(x - m), -x))[:k]
