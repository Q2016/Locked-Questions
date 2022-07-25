Question:
Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change 
exactly one character in this string to match any word in the data structure. Implement the MagicDictionary class:
MagicDictionary() Initializes the object. void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, 
otherwise returns false.
 
Example 1:
Input: ["MagicDictionary", "buildDict", "search", "search", "search", "search"] [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output: [null, null, false, true, false, false]
Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False    








No link

Solution: Dictionary
The basic idea here is very simple: we construct a dictionary, whose key is the length of the given words, and the value is a list containing 
the words with the same length specified in the key. And when we search a word (say word "hello") in the magic dictionary, we only need to 
check those words in dic[len("hellow")], ( named candi in my code). Simple and quite intuitive but beat 90% :-)

class MagicDictionary(object):
    def __init__(self):
        self.wordsdic={}
    def buildDict(self, dict):
        for i in dict:
            self.wordsdic[len(i)]=self.wordsdic.get(len(i),[])+[i]
    def search(self, word):
        for candi in self.wordsdic.get(len(word),[]):
                countdiff=0
                for j in range(len(word)):
                    if candi[j]!=word[j]:
                        countdiff+=1
                if countdiff==1:
                    return True
        return False
                    
        
