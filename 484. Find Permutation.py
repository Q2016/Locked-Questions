Question:
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between 
two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special 
integer array, which contains uniquely all the different number from 1 to n. 
find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]









Solution: Stack (hard if one doesnt find the pattern!)
        
solution is from this link: https://www.youtube.com/watch?v=slFIq997BSE

start with a stack that has [1,2,3,4,5,6,...] and 'result'=[] initially
One has to figure out that a pattern emerges: the number that maps to 'I', you pop from the stack and append it to your 'result'
You always need to add an extra number to the end of the stack
After going through all 'I's and 'D's, append the remaining numbers in the stack
 
example: IDDI                I D D I   
        we start with stack=[1,2,3,4,   5] then above rules give: 
                ans=[1,4,3,2] we add 5 at the end so ans=[1,4,3,2,5]
        
                
        def findPermutation(self, s: str) -> List[int]:
                ans=[]
                stack=[]
                
                for i,c in enumerate(s):
                    stack.append(i+1)
                        
                    if c=='I':
                       while stack:
                           ans.append(stack.pop())
                                                                
                stack.append(len(s)+1)
                while stack:
                    ans.append(stack.pop())
                        
                return ans
                
                
                
                

