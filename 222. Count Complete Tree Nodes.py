Question:
Given the root of a complete binary tree, return the number of the nodes in the tree.
Design an algorithm that runs in less than O(n) time complexity. 

The O(n) solution is:
  
    def countNodes(self, root: Optional[TreeNode]) -> int:      
        if root==None:
            return 0  
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
      
But the problem is asking for less than O(n) so:

  
Solution: Binary Search 
https://leetcode.com/problems/count-complete-tree-nodes/discuss/701466/Python-O(log-n-*-log-n)-solution-with-Binary-Search-explained  
  
I denoted values for nodes in the way of how we are going to count them, note that it does not matter in fact what is inside.
First step is to find the number of levels in our tree.
How we can find the number of elements in last layer? We use binary search, because we know, that elements go from left to right 
in complete binary tree. To reach the last layer we use binary decoding, for example for number 10, we write it as 1010 in binary, 
remove first element (it always will be 1 and we not interested in it), and now we need to take 3 steps: 010, which means left, right, left.
Complexity. To find number of layers we need O(log n). We also need O(log n) iterations for binary search, on each of them we reach the 
bottom layer in O(log n). So, overall time complexity is O(log n * log n). Space complexity is O(log n).

    def Path(self, root, num):
        for s in bin(num)[3:]:
            if s == "0": 
                root = root.left
            else:
                root = root.right
            if not root: return False
        return True
        
    def countNodes(self, root):
        if not root: return 0
        
        left, depth = root, 0
        while left.left:
            left, depth = left.left, depth + 1

        begin, end = (1<<depth), (1<<(depth+1)) - 1
        if self.Path(root,end): return end
        
        while begin + 1 < end:
            mid = (begin + end)//2
            if self.Path(root, mid):
                begin = mid
            else:
                end = mid
        return begin
        
  
