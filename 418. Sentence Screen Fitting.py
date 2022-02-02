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

    def wordsTyping(sentence, rows, cols):
        block=" ".join(sentence)
        l=len(block)
        screen=rows*cols
        "----- ----- ----- -----"
        cursor=0
        repeated=0
        for i in range(rows):
            if l<cols:
                cursor+=cols-l+1 # +1 for space
            elif l>cols and block[cols-1]==" ":
                cursor+=l-cols+1
            elif l>cols and block[cols-1]!=" ":
                n=1
                while block[cols-1-n]!=" ":
                    n+=1
                cursor+=l-cols+n+1
            # for the else: no need to change the cursor
            if cursor>screen:
                return repeated 
            repeated+=1
            


Others:
https://www.youtube.com/watch?v=1ChX4Cpz0bU
