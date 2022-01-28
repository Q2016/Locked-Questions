Question
Assume you have an array of length n initialized with all 0’s and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element 
of subarray A[startIndex … endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.

Example:
Given length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2, 0, 3, 5, 3]
Explanation: Initial state: [ 0, 0, 0, 0, 0 ], After applying operation [1, 3, 2]: [ 0, 2, 2, 2, 0 ], After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ], After applying operation [0, 2, -2]: [-2, 0, 3, 5, 3 ]


Solution:    
# O(N + K)
    def getModifiedArray(self, length, updates):

        res = [0 for _ in range(length)]
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            inc = updates[i][2]  
            res[start] += inc
            if end + 1 < length:
                res[end + 1] += -inc    
        for i in range(1, length):
            res[i] += res[i - 1]
        return res

      
# simulation O(KN)
# Time Limit Exceeded
    def getModifiedArray(self, length, updates):

        res = [0 for _ in range(length)]
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            inc = updates[i][2]
            
            for j in range(start, end + 1):
                res[j] += inc      
        return res
