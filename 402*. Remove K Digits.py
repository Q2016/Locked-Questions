Question:
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

        
        
        
        
        
        
        
We want to pick larger digits ({9}991 or 999{1}) and we are inclined to the left ({9}119 or 911{9})  i.e.
more significant digit. Another case 54321 and 12345 here the choice is clear. The standard method for this
problem is the monotonc stack.

Solution: monotonc stack
        
        https://www.youtube.com/watch?v=cFabMOnJaq0
        

    def removeKdigits(self, num, k):

        stack = []
        for c in num:
            while k>0 and result and result[-1] > c:
                stack.pop()
                k -= 1
            stack.append(d)
        stack=stack[:len(stack)-k]
        res="".join(stack)
        return str(int(res)) if res else "0"
    
    
# Time:  O(n)
# Space: O(n)    
