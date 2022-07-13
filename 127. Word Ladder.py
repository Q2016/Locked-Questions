Question:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the 
shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
    
    

    
    
    
    
    
    
    
    
Solution: BFS

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

    
    
    
Similar question:
Given an int n. You can use only 2 operations:
multiply by 2
integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.    
    
    
    
# using deque for removing first element from the queue in constant time (popleft)
from collections import deque
def num_steps(n):
  # initialize queue with 1
  queue = deque([1])
  no_of_steps = 0

  while(queue):
    no_of_elements_to_remove = len(queue)

    no_of_steps += 1

    for i in range(no_of_elements_to_remove):
      cur_number = queue.popleft()

      muliply_by_2 = int(cur_number * 2) 
      divide_by_3 = int(cur_number / 3)

      if(muliply_by_2 == n or divide_by_3 == n): return no_of_steps

      # append multiplication and division results to queue
      queue.append(muliply_by_2)
      if(divide_by_3 > 0): queue.append(divide_by_3)    
