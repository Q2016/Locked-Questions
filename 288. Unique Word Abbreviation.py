My solution:

from collections import defaultdict

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        
        d = defaultdict(list)
        
        for word in dictionary:
            d[word]= self.abbreviation(self, word)   
        
    
    def isUnique(self, word):
        abb=self.abbreviation(word)
        if abb in self.d:
            return False
        else:
            return True
      
    def abbreviation(self, word):
        l=len(word)
        return word[0]+str(l)+word[-1]
        

dictionary=[ "deer", "door", "cake", "card" ]

vwa = ValidWordAbbr(dictionary)
vwa.isUnique("cane")

      
      
      
      
      
############################################################################
      
https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/unique-word-abbreviation.py      
# Time:  ctor:   O(n), n is number of words in the dictionary. 
#        lookup: O(1)
# Space: O(k), k is number of unique words.

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.lookup_ = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.abbreviation(word)
            self.lookup_[abbr].add(word)
            

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        return self.lookup_[abbr] <= {word}


    def abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
