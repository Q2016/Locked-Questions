Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won’t exceed 100.
Length of each word is greater than 0 and won’t exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:
Input:
rows = 2, cols = 8, sentence = ["hello", "world"]
Output: 
1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:
Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
Output: 
2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
Example 3:
Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
Output: 
1
Explanation:
I-had
apple
pie-I
had--
The character '-' signifies an empty space on the screen.


My solution:
def wordsTyping(sentence, rows, cols):
    
    block=" ".join(sentence)
    
    #print(block)
    l=len(block)
    screen=rows*cols
    
    "----- ----- ----- -----"
    
    cursor=0
    repeated=0
    for i in range(rows):
        if l<cols:
            cursor+=cols-l+1# +1 for space
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
            

rows, cols, sentence = 2, 8, ["hello", "world"]
rows, cols, sentence = 3, 6, ["a", "bcd", "e"]
rows, cols, sentence = 4, 5, ["I", "had", "apple", "pie"]

wordsTyping(sentence, rows, cols)


Others:
https://www.youtube.com/watch?v=1ChX4Cpz0bU
