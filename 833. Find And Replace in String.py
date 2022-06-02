Question:
You are given a string s that you must perform k replacement operations on. 
Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].


Example 1:
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".











Solution: (staright forward based on the description of the question)

class Solution:
    def findReplaceString(self,s:str, indices:List[int], sources:List[str], targets: List[str])->str:
        output=""
        map_l={}
        for i in range(len(indices)):
            map_l[indices[i]]=[sources[i], targets[i]]
        
        indices=sorted(indices)
        i=0
        index=0
        
        while i<len(s):
            if index<len(indices) and i==indices[index]:
                string=map_l[indices[index]][0]
                if i+len(string)<=len(s) and s[i:i+len(string)]==string:
                    output+=map_l[indices[index]][1]
                    i+=len(string)
                index +=1
            else:
                output +=s[i]
                i+=1
        return output
