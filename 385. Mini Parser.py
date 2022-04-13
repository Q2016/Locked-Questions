Question:
Given a nested list of integers represented as a string, implement a parser to deserialize it. Each element is either an 
integer, or a list -- whose elements may also be integers or other lists.

Example:
Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789


            
Solution:            
            
Python using eval:
    
def deserialize(self, s):
    def nestedInteger(x):
        if isinstance(x, int):
            return NestedInteger(x)
        lst = NestedInteger()
        for y in x:
            lst.add(nestedInteger(y))
        return lst
    return nestedInteger(eval(s))            
            
            
            
Parsing char by char
Here I turned the input string into a list with sentinel for convenience.

    def deserialize(self, s):
        def nestedInteger():
            num = ''
            while s[-1] in '1234567890-':
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(nestedInteger())
                if s[-1] == ',':
                    s.pop()
            s.pop()
            return lst
        s = list(' ' + s[::-1])
        return nestedInteger()

    
