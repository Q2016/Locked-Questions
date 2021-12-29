In my opinion an iterator shouldn't copy the entire data (which some solutions have done) but just iterate over the original data structure.

I keep the current progress in a stack. My hasNext tries to find an integer. My next returns it and moves on. I call hasNext in next because hasNext is optional. Some user of the iterator might call only next and never hasNext, e.g., if they know how many integers are in the structure or if they want to handle the ending with exception handling.

Python

Using a stack of [list, index] pairs.

class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = [[nestedList, 0]]

    def next(self):
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
            
    def hasNext(self):
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
