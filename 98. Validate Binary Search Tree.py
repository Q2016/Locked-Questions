Use recursion. Pass down two parameters: lessThan (which means that all nodes in the 
the current subtree must be smaller than this value) and largerThan (all must be larger 
than it). Compare root of the current subtree with these two values. Then, recursively 
check the left and right subtree of the current one. Take care of the values passed down.

class Solution(object):
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and \
               self.isValidBST(root.right, lessThan, max(root.val, largerThan))
