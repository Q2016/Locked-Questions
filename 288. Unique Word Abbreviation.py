Question:
An abbreviation of a word follows the form . Below are some examples of word abbreviations:
a) it                      --> it    (no abbreviation)
     1
b) d|o|g                   --> d1g
              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n
              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation 
is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true


Solution:

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
        


      
      
      
      
      
