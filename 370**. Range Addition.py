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


    
    
    
    
    
    
    
    
    
    
    
Solution: (Nice!)

There is only one read query on the entire range, and it occurs at the end of all update queries. Additionally, the order of processing update 
queries is irrelevant. Therefore, we don’t have to process the entire range until the end of the updates.
Cumulative sums operations apply the effects of past elements to the future elements in the sequence.
Therefore, for every (start, end, val) updates, we only need to do two operations:

arr[start] += val;
arr[end + 1] -= val;
At the end, we apply cumulative sum to the array: array[i] += array[i - 1].

For each update query (start,end,val) on the array arr, the goal is to achieve the result: arri=arri+val∀i∈[start,end].

Applying the final transformation, ensures two things:

It carries over the +val increment over to every element arri∀i≥start.
It carries over the −val increment (equivalently, a +val decrement) over to every element arrj∀j>end.    
    
    
# O(N + K)
    def getModifiedArray(self, length, updates):

        res = [0 for _ in range(length)]
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            c = updates[i][2]  
            res[start] += c
            if end + 1 < length:
                res[end + 1] += -c    # we subtract to neutralize previous +c
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
            c = updates[i][2]
            
            for j in range(start, end + 1):
                res[j] += c      
        return res
