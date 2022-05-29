Question:
Write a function to generate the generalized abbreviations of a word.

Example:
Given word ="word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
test='word'
round 1: ['w','1']
round 2: ['wo','w1','1o','2']
round 3: ['wor','wo1','w1r',...]


    
    
    
    
    
    
    
    
    
Solution: backtracking

    def backtracking(self, word: str, asf: str, count:int, pos:int):
        
        if count>0:
            backtracking(word, asf + count + word[pos], 0, pos+1)
        else:
            backtracking(word, asf + word[pos], 0, pos+1)
            
        backtracking(word, asf, count+1, pos+1)
        
        
    def solution(self):
        backtracking(word, "", 0, 0)
