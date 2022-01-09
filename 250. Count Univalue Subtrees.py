This question is not well done, and the idea is already there, but I always make mistakes in logic. I am really a pig brain.

In traverse, there are two points when judging whether a node is a uni-value tree:
His left and right subtrees are uni-value trees;
It is equal to the value of the left and right subtrees.
is indispensable. .

Once it is a uni-value tree, the total number is ++. .

But when comparing the subtree VALUE, it involves the case that the subtree is NULL, and one more case is judged to be not NULL. In the beginning, I wanted to write a line, the logic was messed up, the pretense failed, and I was beaten in the face.

public class Solution 
{
    int res = 0;
    public int countUnivalSubtrees(TreeNode root) 
    {
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        helper(root);
        return res;
    }
    
    public boolean helper(TreeNode root)
    {
        if(root == null) return true;
        
        boolean left = helper(root.left);
        boolean right = helper(root.right);
        
        if(left && right)
            if((root.left == null || root.left.val == root.val) && (root.right ==null || root.right.val == root.val))
                res++;
            else return false;
        
        return left && right;
        
    }

}

/*
[1,-2,3,-2,null,null,null,null,5]
[5,1,5,5,5,null,5]
[5,1,5,5,5,1,1]
[5,5,5,5,5,5,5]
[7,82,82,-79,98,98,-79,-79,null,-28,-24,-28,-24,null,-79,null,97,65,-4,null,3,-4,65,3,null,97]

*/
Second brush.

Count the number of subtrees where all vals are equal. For example, [2,2] itself is one, and then there is another leaf, so there are two. The example given is a good illustration of what is going on. .

Still the same as the previous one, bottom-up via post order traversal.

The information that needs to be passed on is:

Am I unique-value-subtree.
Gone. Or my root.val, but it can be obtained directly from root.left.val or root.right.val above, so it is not passed up.
So there is only 1) this information, then there is no need to create a new class.

It's a bit similar to the two I made today, 124 and 333, but simpler than those two.

I made a mistake at the beginning, thinking it was the sum of the total node, but it is not that complicated, just the sum of the subTree.

Time: O(n)
Space: O(n)

public class Solution {
    int res = 0;
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        postOrder(root);
        return res;
    }
    
    public boolean postOrder(TreeNode root) {
        if (root == null) return true;
        
        boolean left = postOrder(root.left);
        boolean right = postOrder(root.right);
        
        if (left && right) {
            if ((root.left == null || root.val == root.left.val) && 
                (root.right == null || root.val == root.right.val)) {
                    res ++;
                    return true;
            }
        } 
        
        return false;
        
    }
}
