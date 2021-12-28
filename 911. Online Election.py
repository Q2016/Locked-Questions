Approach 1: List of Lists + Binary Search
Intuition and Algorithm

We can store the votes in a list A of lists of votes. Each vote has a person and a timestamp, 
and A[count] is a list of the count-th votes received for that person.

Then, A[i][0] and A[i] are monotone increasing, so we can binary search on them to find the most recent vote by time.

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        self.A = []
        self.count = collections.Counter()
        for p, t in zip(persons, times):
            self.count[p] = c = self.count[p] + 1
            while len(self.A) <= c: self.A.append([])
            self.A[c].append((t, p))

    def q(self, t):
        lo, hi = 1, len(self.A)
        while lo < hi:
            mi = (lo + hi) / 2
            if self.A[mi][0][0] <= t:
                lo = mi + 1
            else:
                hi = mi
        i = lo - 1
        j = bisect.bisect(self.A[i], (t, float('inf')))
        return self.A[i][j-1][1]
        
Complexity Analysis

Time Complexity: O(N + Q \log^2 N)O(N+Qlog^2 N), where NN is the number of votes, and QQ is the number of queries.

Space Complexity: O(N)O(N).



Approach 2: Precomputed Answer + Binary Search
Intuition and Algorithm

As the votes come in, we can remember every event (winner, time) when the winner changes. After, 
we have a sorted list of these events that we can binary search for the answer.

class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in itertools.izip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t):
        i = bisect.bisect(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]
