Question:
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder 
is the postorder traversal of the same tree, reconstruct and return the binary tree.
If there exist multiple answers, you can return any of them.    
    
 
Solution:  Recursive
    
class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre or not post: return None
        root = TreeNode(pre[0])
        if len(post) == 1: return root
        idx = pre.index(post[-2])
        root.left = self.constructFromPrePost(pre[1: idx], post[:(idx - 1)])
        root.right = self.constructFromPrePost(pre[idx: ], post[(idx - 1):-1])
        return root
    
The first element in "pre" and the last element in "post" should both be the value of the root. The second to last of "post" should 
be the value of right child of the root. So we can find the index to split "left" and "right" children in "pre". Don't forget to evaluate 
if the length of "post" is larger than 1, since we used post[-2].    
