Question:
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number 
of times it appears in the string. Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.    









Solution: Counter & Bucket Sort (similar to 347.)

	https://www.youtube.com/watch?v=trFw8IDw2Vg
	
	
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        bucket = [[] for _ in range(n+1)]
        for c, freq in cnt.items():
            bucket[freq].append(c)
        
        ans = []
        for freq in range(n, -1, -1):
            for c in bucket[freq]:
                ans.append(c * freq)
        return "".join(ans)

Since freq values are in range [0...n], so we can use Bucket Sort to achieve O(N) in Time Complexity.
Time:  O(n)
Space: O(n)    


HashTable + Heap:
    
def frequencySort(self, s: str) -> str:
	# Count the occurence on each character
	cnt = collections.Counter(s)
	
	# Build heap
	heap = [(-v, k) for k, v in cnt.items()]
	heapq.heapify(heap)
	
	# Build string
	res = []
	while heap:
		v, k = heapq.heappop(heap)
		res += [k] * -v
	return ''.join(res)

Time Complexity: O(nlogk), where k is the number of distinct character.
Space Complexity: O(n)
