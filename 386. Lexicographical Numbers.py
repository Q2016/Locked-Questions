Question:
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order. You must write an algorithm that runs 
in O(n) time and uses O(1) extra space.  For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].


Solution:
The idea is pretty simple. If we look at the order we can find out we just keep adding digit from 0 to 9 to every digit and make it a tree.
Then we visit every node in pre-order. 
       1        2        3    ...
      /\        /\       /\
   10 ...19  20...29  30...39   ....    
    
    
    def lexicalOrder(self, n):
         self.res = []
         for i in range(1, 10):
             self.helper(i, n)
         return self.res
    
    def helper(self, start, end):
        if start > end:
            return
        self.res.append(start)
        for i in range(0, 10):
            if 10 * start + i > end:
                return
            self.helper(10 * start + i, end)
            
Time O(n)
Space O(logn)
