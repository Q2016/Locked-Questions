Question:
Given an array of strings words and an integer k, return the k most frequent strings. Return the answer sorted by the frequency 
from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.    








No link

Solution: 
    
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        result = sorted(counts, key=lambda word: (-counts[word], word))
        return result[:k]    

# or:

    def topKFrequent(self, words, k):
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        ret = sorted(d, key=lambda word: (-d[word], word)) 
        return ret[:k]    
    
    
   

    
    
    Heap
    
import collections
import heapq
import functools

@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)   
        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]
