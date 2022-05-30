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
From this link: https://www.youtube.com/watch?v=1ChX4Cpz0bU
    
    
    
    def wordsTyping(sentence, rows, cols):
        sentence=" ".join(sentence) # adding space between words
        sentenceLen=len(sentence)
        
        cursor=0
        for row in range(rows):
            cursor +=cols
            if sentence[cursor%sentenceLen] == ' ':
                cursor+=1
            else:
                while (cursor>=0 and sentence[cursor%sentenceLen] != ' '):
                    cursor-=1
                cursor+=1
                
         return cursor/sentenceLen
                   
        

            


