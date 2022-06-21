Question:
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.  

Example:  
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true  
  
  
  
  
  
  
  
  
  
  
Solution: 
# Brute force: find all permutations of interleaving meaning:   
We start by taking the current character of the first string s1s1 and then appending all possible interleavings of the remaining 
portion of the first string s1s1 and the second string s2s2 and comparing each result formed with the required interleaved string s3s3. 
Similarly, we choose one character from the second string s2s2 and form all the interleavings with the remaining portion of s2s2 and s1s1 
to check if the required string s3s3 can be formed.  
  
  
  
  
#backtrack 
    def isInterleave(self, s1: str, s2: str, s3: str):
        def backtrack(a,b,c):
            if not a and not b:
                if not c:
                    return True
                else:
                    return False
            if a and c and  a[0]==c[0]:
                if  backtrack(a[1:],b,c[1:]):
                    return True
            if b and c and b[0]==c[0]:
                if  backtrack(a,b[1:],c[1:]):
                    return True
            return False
        if len(s1)+len(s2)!=len(s3):
            return False
        return backtrack(s1,s2,s3)
		
    
Complexity Analysis

Time complexity : O(2^(m+n)). m is the length of s1 and n is the length of s2.

Space complexity : O(m+n). The size of stack for recursive calls can go upto m+n.    
    
    
		
#introduce memorization for each string state 
    def isInterleave(self, s1: str, s2: str, s3: str):
        cache ={}
        def backtrack(a,b,c):
            if not a and not b:
                if not c:
                    return True
                else:
                    return False
            if (a,b,c)  not in cache:            
                if a and c and  a[0]==c[0]:
                    if  backtrack(a[1:],b,c[1:]):
                        cache[(a,b,c)]=True
                        return True
                if b and c and b[0]==c[0]:
                    if  backtrack(a,b[1:],c[1:]):
                        cache[(a,b,c)]=True
                        return True
                cache[(a,b,c)]=False
            return cache[(a,b,c)]
        if len(s1)+len(s2)!=len(s3):
            return False
        return backtrack(s1,s2,s3)  
      
      
      
Time complexity: O(m⋅n), where mm is the length of s1s1 and nn is the length of s2. That's a consequence of the fact that each (i, j) 
                  combination is computed only once.

Space complexity: O(m⋅n) to keep double array memo.      
