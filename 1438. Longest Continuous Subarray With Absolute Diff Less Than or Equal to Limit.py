https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)


Intuition
Last week we learned,
in 1425. Constrained Subsequence Sum
how to get minimum in a subarray when sliding.

This week, we need to get both the maximum and the minimum,
at the same time.

So I opened my post last week,
and copy some my own codes.


Solution 0: Binary insert and remove
Keep an increasing list L.
Binary insert the current element.
If the L[L.size() - 1] - L[0] > limit,
binary search the position of A[i] and remove it from the list.

Time O(N^2)
Space O(N)


    def longestSubarray(self, A, limit):
        i, L = 0, []
        for j in xrange(len(A)):
            bisect.insort(L, A[j])
            if L[-1] - L[0] > limit:
                L.pop(bisect.bisect(L, A[i]) - 1)
                i += 1
        return j - i + 1

Solution 1: Use two heaps
Time O(NogN)
Space O(N)


Python

    def longestSubarray(self, A, limit):
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i: heapq.heappop(maxq)
                while minq[0][1] < i: heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res

Solution 2: Use TreeMap
Use one tree map can easily get the maximum and the minimum at the same time.
In java, we can use TreeMap to count elements.
In cpp, it suports multi treeset, that's even better.

Time O(NogN)
Space O(N)

Java
@prdp89

public int longestSubarray(int[] A, int limit) {
    int i = 0, j;
    TreeMap<Integer, Integer> m = new TreeMap<>();
    for (j = 0; j < A.length; j++) {
        m.put(A[j], 1 + m.getOrDefault(A[j], 0));
        if (m.lastEntry().getKey() - m.firstEntry().getKey() > limit) {
            m.put(A[i], m.get(A[i]) - 1);
            if (m.get(A[i]) == 0)
                m.remove(A[i]);
            i++;
        }
    }
    return j - i;
}
C++

    int longestSubarray(vector<int>& A, int limit) {
        int i = 0, j;
        multiset<int> m;
        for (j = 0; j < A.size(); ++j) {
            m.insert(A[j]);
            if (*m.rbegin() - *m.begin() > limit)
                m.erase(m.find(A[i++]));
        }
        return j - i;
    }

Solution 3: Use two deques
Time O(N)
Space O(N)


Java

    public int longestSubarray(int[] A, int limit) {
        Deque<Integer> maxd = new ArrayDeque<>();
        Deque<Integer> mind = new ArrayDeque<>();
        int i = 0, j;
        for (j = 0; j < A.length; ++j) {
            while (!maxd.isEmpty() && A[j] > maxd.peekLast()) maxd.pollLast();
            while (!mind.isEmpty() && A[j] < mind.peekLast()) mind.pollLast();
            maxd.add(A[j]);
            mind.add(A[j]);
            if (maxd.peek() - mind.peek() > limit) {
                if (maxd.peek() == A[i]) maxd.poll();
                if (mind.peek() == A[i]) mind.poll();
                ++i;
            }
        }
        return j - i;
    }
C++

    int longestSubarray(vector<int>& A, int limit) {
        deque<int> maxd, mind;
        int i = 0, j;
        for (j = 0; j < A.size(); ++j) {
            while (!maxd.empty() && A[j] > maxd.back()) maxd.pop_back();
            while (!mind.empty() && A[j] < mind.back()) mind.pop_back();
            maxd.push_back(A[j]);
            mind.push_back(A[j]);
            if (maxd.front() - mind.front() > limit) {
                if (maxd.front() == A[i]) maxd.pop_front();
                if (mind.front() == A[i]) mind.pop_front();
                ++i;
            }
        }
        return j - i;
    }
Python

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

More Similar Sliding Window Problems
Here are some similar sliding window problems.
Also find more explanations.
If you have question about the complexity and if/while clause,
pick an easier one first.

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

More Good Stack Problems
Here are some stack problems that impressed me.

Constrained Subsequence Sum
Minimum Cost Tree From Leaf Values
Sum of Subarray Minimums
Online Stock Span
Score of Parentheses
Next Greater Element II
Next Greater Element I
Largest Rectangle in Histogram
Trapping Rain Water

FAQ
Q: Why doest the return value work? Why use if instead of while
A: Please refer to the discussion of @hzfmer
(Maybe I should summary up an explanation)

Q: Is your first thought compared with what @hzfmer suggests?
A: If you follow my posts, you'll know that I use them everywhere.
