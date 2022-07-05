Question:
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz". Given a list of strings 
which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example: 
Given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:[  ["abc","bcd","xyz"],  ["az","ba"],   ["acef"],  ["a","z"] ]
Note: For the return value, each inner list's elements must follow the lexicographic order.

Hints:things to consider: 
1 does each group allow duplicates, such as ["a", "a"]. 
2 how to calculate unique hash key.
  
  
  
  
  
  
  
Group by length and then pick two words and see if the number of shifts is consistent for all charachters of the two words  

Solution: Dictionary
  
Comment from anoter solution:  
This problem is very easy.
The basic idea is to shift all words back into the form starting with 'a'. (all digits must shift the same distance). 
If the two words share the same shifted word, it means they actually come from the same shift group. 


    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
      groups = collections.defaultdict(list)
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                key += ((26+ ord(s[i+1]) - ord(s[i])) % 26,)
            groups[key] = groups.get(key,[])+[s]

        return groups.values()
