Question:
Given an array of integers nums and a positive integer k, check whether it is possible to 
divide this array into sets of k consecutive numbers.
Return true if it is possible. Otherwise, return false.

Example 1:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
    
    
Solution: Greedy Algo

Solution 1
Count number of different cards to a map c
Loop from the smallest card number.
Everytime we meet a new card i, we cut off i - i + k - 1 from the counter.

Complexity:
Time O(MlogM + MK), where M is the number of different cards.
In Cpp and Java it's O(NlogM), which can also be improved.

    def isPossibleDivide(self, A, k):
        c = collections.Counter(A)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True
        

Follow Up
We just got lucky AC solution. Because k <= 10000.
What if k is huge, should we cut off card on by one?


Solution 2
Count number of different cards to a map c
Cur represent current open straight groups.
In a deque start, we record the number of opened a straight group.
Loop from the smallest card number.
For example, A = [1,2,3,2,3,4], k = 3
We meet one 1:
opened = 0, we open a new straight groups starting at 1, push (1,1) to start.
We meet two 2:
opened = 1, we need open another straight groups starting at 1, push (2,1) to start.
We meet two 3:
opened = 2, it match current opened groups.
We open one group at 1, now we close it. opened = opened - 1 = 1
We meet one 4:
opened = 1, it match current opened groups.
We open one group at 2, now we close it. opened = opened - 1 = 0

return if no more open groups.

Complexity
O(N+MlogM), where M is the number of different cards.
Because I count and sort cards.
In Cpp and Java it's O(NlogM), which can also be improved.

    def isPossibleDivide(self, A, k):
        c = collections.Counter(A)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == k: opened -= start.popleft()
        return opened == 0
