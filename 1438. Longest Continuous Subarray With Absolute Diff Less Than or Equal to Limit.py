Question:
Given an array of integers nums and an integer limit, return the size of the longest non-empty 
subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.    


Solution: Deques
    
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)

Last week we learned, in 1425. Constrained Subsequence Sum how to get minimum in a subarray when sliding.
This week, we need to get both the maximum and the minimum, at the same time.

    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i

Time O(N)
Space O(N)




(1425. Constrained Subsequence Sum -- Hard
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every 
two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining 
elements in their original order.)

(239. Sliding Window Maximum -- Hard
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.)

(209. Minimum Size Subarray Sum -- Medium
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray 
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.)

(862. Shortest Subarray with Sum at Least K -- Hard
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. 
If there is no such subarray, return -1. A subarray is a contiguous part of an array.)
    
    

Solution to related problems: (sliding windows)   
    
    
1425. Constrained Subsequence Sum

We need to know the maximum in the window of size k.
Use heqp will be O(NlogN)
Use TreeMap will be O(NlogK)
Use deque will be O(N)

Explanation
Update res[i],
where res[i] means the maximum result you can get if the last element is A[i].
I directly modify on the input A,
if you don't like it,
use a copy of A
Keep a decreasing deque q,
deque[0] is the maximum result in the last element of result.
If deque[0] > 0. we add it to A[i]
In the end, we return the maximum res.

Complexity
Because all element are pushed and popped at most once.
Time O(N)
Because at most O(K) elements in the deque.
Space O(K)

    def constrainedSubsetSum(self, A, k):
        deque = collections.deque()
        for i in xrange(len(A)):
            A[i] += deque[0] if deque else 0
            while len(deque) and A[i] > deque[-1]:
                deque.pop()
            if A[i] > 0:
                deque.append(A[i])
            if i >= k and deque and deque[0] == A[i - k]:
                deque.popleft()
        return max(A)
    
    
    
    
    
239. Sliding Window Maximum

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        # Checking for base case
        if not nums:
            return []
        if k == 0:
            return nums
        # Defining Deque and result list
        deq = deque()
        result = []
        # First traversing through K in the nums and only adding maximum value's index to the deque.
        # Note: We are olny storing the index and not the value.
        # Now, Comparing the new value in the nums with the last index value from deque,
        # and if new valus is less, we don't need it
        for i in range(k):
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)
        # Here we will have deque with index of maximum element for the first subsequence of length k.
        # Now we will traverse from k to the end of array and do 4 things
        # 1. Appending left most indexed value to the result
        # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
        # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
        # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
        for i in range(k, len(nums)):
            result.append(nums[deq[0]])
            if deq[0] < i - k + 1:
                deq.popleft()
            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)
        #Adding the maximum for last subsequence
        result.append(nums[deq[0]]) 
        return result
    
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;
        for (int i=0; i<nums.size(); i++) {
            if (!dq.empty() && dq.front() == i-k) dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i])
                dq.pop_back();
            dq.push_back(i);
            if (i>=k-1) ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};    


209. Minimum Size Subarray Sum

The result is initialized as res = n + 1.
One pass, remove the value from sum s by doing s -= A[j].
If s <= 0, it means the total sum of A[i] + ... + A[j] >= sum that we want.
Then we update the res = min(res, j - i + 1)
Finally we return the result res

    def minSubArrayLen(self, s, A):
        i, res = 0, len(A) + 1
        for j in xrange(len(A)):
            s -= A[j]
            while s <= 0:
                res = min(res, j - i + 1)
                s += A[i]
                i += 1
        return res % (len(A) + 1)   
    
    
    
862. Shortest Subarray with Sum at Least K    

Calculate prefix sum B of list A.
B[j] - B[i] represents the sum of subarray A[i] ~ A[j-1]
Deque d will keep indexes of increasing B[i].
For every B[i], we will compare B[i] - B[d[0]] with K.

Complexity:
Every index will be pushed exactly once.
Every index will be popped at most once.
Time O(N)
Space O(N)

How to think of such solutions?
Basic idea, for array starting at every A[i], find the shortest one with sum at leat K.
In my solution, for B[i], find the smallest j that B[j] - B[i] >= K.
Keep this in mind for understanding two while loops.

What is the purpose of first while loop?
For the current prefix sum B[i], it covers all subarray ending at A[i-1].
We want know if there is a subarray, which starts from an index, ends at A[i-1] and has at least sum K.
So we start to compare B[i] with the smallest prefix sum in our deque, which is B[D[0]], hoping that [i] - B[d[0]] >= K.
So if B[i] - B[d[0]] >= K, we can update our result res = min(res, i - d.popleft()).
The while loop helps compare one by one, until this condition isn't valid anymore.

Why we pop left in the first while loop?
This the most tricky part that improve my solution to get only O(N).
D[0] exists in our deque, it means that before B[i], we didn't find a subarray whose sum at least K.
B[i] is the first prefix sum that valid this condition.
In other words, A[D[0]] ~ A[i-1] is the shortest subarray starting at A[D[0]] with sum at least K.
We have already find it for A[D[0]] and it can't be shorter, so we can drop it from our deque.

What is the purpose of second while loop?
To keep B[D[i]] increasing in the deque.

Why keep the deque increase?
If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
B[i] can help us make the subarray length shorter and sum bigger. So no need to keep d.back() in our deque.
    
    def shortestSubarray(self, A, K):
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1    
    
    
    
    
    
More Similar Sliding Window Problems:

Constrained Subsequence Sum
Number of Substrings Containing All Three Characters
Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum


More Good Stack Problems:

Constrained Subsequence Sum
Minimum Cost Tree From Leaf Values
Sum of Subarray Minimums
Online Stock Span
Score of Parentheses
Next Greater Element II
Next Greater Element I
Largest Rectangle in Histogram
Trapping Rain Water

