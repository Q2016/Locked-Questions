Question:
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.    


Solution: Recursion
If root1 and root2 have the same root value, then we only need to check if their children are equal (up to ordering.)
There are 3 cases:
If root1 or root2 is null, then they are equivalent if and only if they are both null.
Else, if root1 and root2 have different values, they aren't equivalent.
Else, let's check whether the children of root1 are equivalent to the children of root2. There are two different ways to pair these children.

class Solution(object):
    def flipEquiv(self, root1, root2):
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or  \\
                self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
