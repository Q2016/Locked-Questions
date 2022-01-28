Question
Given an array of integers citations where citations[i] is the number of citations a researcher received for 
their ith paper, return compute the researcher's h-index. Definition of h-index: A scientist has an index h if 
h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
If there are several possible values for h, the maximum one is taken as the h-index.

Example 1:
Input: citations = [3,0,6,1,5], Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

    # Counting sort.
    def hIndex(self, citations):
        n = len(citations);
        count = [0] * (n + 1)
        for x in citations:
            # Put all x >= n in the same bucket.
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1

        h = 0
        for i in reversed(xrange(0, n + 1)):
            h += count[i]
            if h >= i:
                return i
        return h

# Time:  O(n)
# Space: O(1)    
    

    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h


# Time:  O(nlogn)
# Space: O(1)    
