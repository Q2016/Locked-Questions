Question:
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given 
sentence can be fitted on the screen. Note: A word cannot be split into two lines. The order of words in the sentence must 
remain unchanged. Two consecutive words in a line must be separated by a single space.

Example 1:
Input: rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"], Output: 1
Explanation:
I-had
apple
pie-I
had--
The character '-' signifies an empty space on the screen.










Solution:
From this link: https://www.youtube.com/watch?v=e987rKv1d7E
    
    
class Solution:    
    def wordsTyping(sentence, rows, cols):
        s=' '.join(sentence)+' ' # tricky
        n=len(s)
        total_len=0
        
        for _ in range(rows):
            total_len +=cols
            
            if s[total_len%n]==' ': # tricky
                total_len +=1
            else:
                while s[(total_len-1)%n] !=' ' and total_len>0: # tricky
                    total_len -=1
        
        return total_len//n

                   
Time complexity: O(rows*len of the longest word)        

            


