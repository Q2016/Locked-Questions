class Solution:
    def reverseWords(self, s: str) -> str:
        
        mystring=s.split()[::-1]
        
        newstring=''
        for word in mystring:
            newstring=newstring+word+' '
        
        
        return newstring[:-1]
