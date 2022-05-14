Question:
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, 
the result should equal the sorted array. Return the largest number of chunks we can make to sort the array.

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

    
Solution:    
    
Explanation:
Many solutions simply describe how to know when we can add a count to the total number of chunks (when max == index), but not why it works.
We know the final position of the elements in the array: their sorted positions. Since the array consists of elements from [0, N-1], for any 
value in the array, the corresponding index is where that element must end up in the end. This is how we will decide when we should chunk our elements.

We want to maximize the number of chunks in our array. But we just said for any value in the array, it must end up in its corresponding 
index at the end. So the chunk we put that value in must cover at least that index, so that after sorting that chunk, it can be in that index.
If we encounter an element v1 initially at index i1, where v1 > i1, then for the chunk containing element v1, it must at least contain index v1, 
so that when we sort that chunk, v1 will move to index v1. Since we are still at i1, we cannot end the chunk for this element until we reach at 
least v1. We should keep track of this minimum using a variable, say min_index_for_chunk_end.
If we encounter an element v2 initially at index i2, where v2 < i2, then for the chunk containing element v2, it must contain at least index v2. 
Since v2 was already encountered before this, we can consider ending the chunk here. However, we might have other elements in the chunk that have 
a minimum index that is after i2. Luckily we kept track of the minimum index of all previous elements in the chunk using min_index_for_chunk_end. 
We can only end the chunk here if min_index_for_chunk_end == i2.

    def maxChunksToSorted(self, arr):
        chunks = 0
        min_index_for_chunk_end = arr[0]
        for i in xrange(len(arr)):
            min_index_for_chunk_end = max(min_index_for_chunk_end, arr[i])
            if i == min_index_for_chunk_end:
                chunks += 1
        return chunks
