Question:
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between 
two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special 
integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). 
For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] (not 1 to n property)
or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.
On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer 
to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the 
number 1 and 2 construct an increasing relationship.

Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]





Solution: Stack
Because of the second constraint, we could think that we want to have the permutation close to the increasing order like [1, 2, 3, 4, 5] 
when the input is ‘IDDI’. The idea is that we consider ‘I’ as the border to separate the decreasing regions and increasing regions. 
And we store the numbers we want to add in the stack. We can think about the stack when we see questions related to the reverse string.
We then put the number into the stack when we encounter ‘D’ because we need to reverse them. Once we encounter ‘I’, it means that the 
reverse ends, so we pop out all the numbers in the stack. We start from 1 and put the current number into the stack. The first command 
is ‘I’. It means that we want to have a number larger than 1. So we pop 1 out of the stack and add it into the output list. Then add the 
current number 2 into the stack. The second command is ‘D’, so we add 3 into the stack. Now the stack contains [2, 3].
The third command is also ‘D’, then we add 4 into the stack as well. Now the stack contains [2, 3, 4].
The fourth command is ‘I’. Now we can stop the reversing. So we pop out all the numbers in the stack and add them into output. 
After pop out all the numbers, the output is [1, 4, 3, 2]. After pop out all the numbers, we add 5 into the stack as well.
In the end, we just need to pop out all the numbers in the stack and add them to the output list. We finally get [1, 4, 3, 2, 5].

        def findPermutation(self, s: str) -> List[int]:
            n = len(s) + 1
            stack = [1]
            cur = 1
            output = []
            for i in s:
                cur += 1
                if i == 'D':
                    stack.append(cur)
                else:
                    while stack:
                        output.append(stack.pop())
                    stack.append(cur)
            while stack:
                output.append(stack.pop())
        return output
