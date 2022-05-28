Question:
Given a binary tree, count the number of uni-value subtrees. A Uni-value subtree means all nodes of the subtree have the same value.

For example: Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5
return 4.    








Solution: bottom-up Postorder (educational, post-order makes sense since it starts from the leaves)

In traverse, there are two points when judging whether a node is a uni-value tree:
His left and right subtrees are uni-value trees;
It is equal to the value of the left and right subtrees.

1) The first solution wont work

    res = 0;
    def countUnivalSubtrees(TreeNode root) 
        if(root == null) return 0;
        if(root.left == null && root.right == null) return 1;
        helper(root);
        return res;
    
    def helper(TreeNode root)
        if(root == null) return true;
        
        boolean left = helper(root.left);
        boolean right = helper(root.right);
        
        if(left && right)
            if((root.left == null || root.left.val == root.val) && (root.right ==null || root.right.val == root.val))
                res++;
            else return false;        
        return left and right;

2) Second brush.

Similar to problems 124 and 333, but simpler than those two. I made a mistake at the beginning, thinking it was 
the sum of the total node, but it is not that complicated, just the sum of the subTree.

    res = 0;
    def countUnivalSubtrees(TreeNode root) 
        if (root == null) return 0;
        postOrder(root);
        return res;
    
    def postOrder(TreeNode root) 
        if (root == null) return true;
        
        boolean left = postOrder(root.left);
        boolean right = postOrder(root.right);
        
        if (left && right) 
            if ((root.left == null || root.val == root.left.val) && (root.right == null || root.val == root.right.val)) 
                    res ++;
                    return true;
        return false;


Time: O(n)
Space: O(n)
