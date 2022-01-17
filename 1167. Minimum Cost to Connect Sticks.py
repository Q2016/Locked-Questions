Explain
https://www.youtube.com/watch?v=3dqR2nYElyw


You have some sticks with positive integer lengths.

You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  
You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:

Input: sticks = [2,4,3]
Output: 14
Example 2:

Input: sticks = [1,8,3,5]
Output: 30



Intuition:
This is a direct application of the Huffman Coding algorithm. In this problem, each stick's 
length is the equivalence of character frequency, the goal here is to merge all sticks into one 
stick with the minimum cost, this is essentially the same with building a Huffman tree with minimum cost. 
Each merge operation merges two meta-sticks(two subtrees) into one subtree with the introduction of a 
new internal tree node. The gist of the Huffman Coding is to greedily pick the 2 least frequent characters 
and merge them, then recursively solve a smaller problem with 1 fewer character. In this problem, this 
translates into picking the 2 least stick lengths.


The Heaps are binary trees that the parent nodes have values less or equal to its children. In Python, 
the min heap (priority queues) can be built using the heapq functions. For example, the heapq.heapify will 
transform a list into heap, in place. And the heapq.heappop returns the current minimum element in the heap 
while heapq.heappush adds a new item to the heap.


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            heapq.heappush(sticks, a + b)
            res += a + b
        return res

