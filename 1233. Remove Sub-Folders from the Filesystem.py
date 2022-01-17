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
