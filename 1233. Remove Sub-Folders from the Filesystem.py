Question:
Given a list of folders folder, return the folders after removing all sub-folders in those folders. 
 
Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.   
    
    
    
    
Solution: 
 
Method 1: sort by length then put only parent into HashSet

Sort folder by length;
Check if the floder's parent fold in HashSet before adding it into the HashSet.
Note: the part before any / is a parent.
 
     def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda f: len(f))
        seen = set()
        for f in folder:
            for i in range(2, len(f)):
                if f[i] == '/' and f[: i] in seen:
                    break
            else:
                seen.add(f)
        return list(seen)
 
Analysis
Sort cost n * logn;
Outer for loop run n times; inner for loop cost i in each iteration due to substring(0, i), that is, 2 + ... + m, which is O(m ^ 2);
Therefore,

Time: O(n * (logn + m ^ 2)), space: (n * m), where n = folder.length, m = average size of the strings in folder.
  
  
  
Compare the first two methods

Generally speaking, m > logn,

For method 2:
O(n * m * logn)

For method 1:
O(n * (logn + m ^ 2)) = O(n * m ^ 2) > O(n * m * logn) - time complexity of method 1.

Conclusion:

Method 2 is more space efficent and is, generally speaking, faster than method 1;
Method 1 is faster if folders' average size m < logn.  
 
 
 
 
Method 2: Trie 

Please see and vote for my solutions for
208. Implement Trie (Prefix Tree)
1233. Remove Sub-Folders from the Filesystem
1032. Stream of Characters
211. Add and Search Word - Data structure design
676. Implement Magic Dictionary
677. Map Sum Pairs
745. Prefix and Suffix Search
425. Word Squares

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True  
    
    def find(self):
        def dfs(direc, node):
            if node.isEnd:
                answer.append('/' + '/'.join(direc))
                return
            for char in node.children:
                dfs(direc + [char], node.children[char])
        
        answer = []
        dfs([], self.root)
        return answer


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            f = f.split('/')[1:]
            trie.insert(f)
        return trie.find()
