Question:
Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters 
of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
Output: true    

    
    
    
    
    
    
    
    
Solution: Backtracking
    
In general I think this problem do not have polynomial solution, so we need to check a lot of possible options. What should we use in this case: 
it is bruteforce, with backtracking. Let dfs(ind, i, j) be our backtracking function, where i and j are coordinates of cell we are currently 
in and ind is index of letter in word we currently in. Then our dfs algorithm will look like:

First, we have self.Found variable, which helps us to finish earlier if we already found solution.
Now, we check if ind is equal to k - number of symbols in word. If we reach this point, it means we found word, so we put self.Found to True 
and return back.
If we go outside our board, we return back.
If symbol we are currently on in words is not equal to symbol in table, we also return back.
Then we visit all neibours, putting board[i][j] = "#" before - we say in this way, that this cell was visited and changing it back after.
What concerns main function, we need to start dfs from every cell of our board and also I use early stopping if we already found word.



class Solution:
    def exist(self, board, word):
        
        def dfs(ind, i, j):
            if self.Found: return        #early stop if word is found
            if ind == k:
                self.Found = True                #for early stopping
                return 
            if i < 0 or i >= m or j < 0 or j >= n: return 
            tmp = board[i][j]
            if tmp != word[ind]: return
            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(ind + 1, i+x, j+y)
            board[i][j] = tmp
        
        self.Found = False
        m, n, k = len(board), len(board[0]), len(word)
        for i, j in product(range(m), range(n)):
            if self.Found: return True          #early stop if word is found
            dfs(0, i, j)
        return self.Found  

    
Complexity: 
Time complexity is potentially O(m*n*3^k), where k is length of word and m and n are sizes of our board: we start from all possible 
cells of board, and each time (except first) we can go in 3 directions (we can not go back). In practice however this number will be usually 
much smaller, because we have a lot of dead-ends. 
Space complexity is O(k) - potential size of our recursion stack. If you think this analysis 
can be improved, please let me know!    
