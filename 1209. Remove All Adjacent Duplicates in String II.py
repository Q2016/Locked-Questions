Question:
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent 
and equal letters from s and removing them, causing the left and the right side of the deleted 
substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. 

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"     









Solution: Stack or Two pointers (Similar to 1047)

Stack:
     
Save the character c and its count to the stack.
If the next character c is same as the last one, increment the count.
Otherwise push a pair (c, 1) into the stack.
I used a dummy element ('#', 0) to avoid empty stack.     
     
    def removeDuplicates(self, s, k):
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

Complexity
Time O(N) for one pass
Space O(N)
