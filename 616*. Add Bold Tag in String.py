Question:
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b>and </b> to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags 
are consecutive, you need to combine them.

Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"



Solution:
    https://www.youtube.com/watch?v=4JPKLcpggCE
        
class Solution:
    
    def addBoldTag(self, s, dict):
        n=len(s)
        
        flag=[0]*n
        cur_end=0
        
        for i in range(n):
            for w in dict:
                if s.startwith(w,i):
                    cur_end=max(cur_end, i+len(w))
            
            flag[i]=i<cur_end
            
        ans=None
        
        for i in range(n):
           
            if flag[i] and (i==0 or (i>0 and not flag[i-1])):
                ans+='<b>'

            ans +=s[i]

            if flag[i] and (i==n-1 or (i<n-1 and not flag[i+1])):
                ans +='</b>'
                    
        return ans
            



# Time:  O(n * d * l), l is the average string length
# Space: O(n)
