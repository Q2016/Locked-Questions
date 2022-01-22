Question:
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Example1:
	
Input: root = [3,5,1,6,2,0,8,null,null,7,4]

	3
      /    \     
     5	     1
   /   \    /  \
  6    2   0    8 
      / \      
     7   4	

	
	
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.



Solution: Preorder



class Solution {
public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        if(!root)
            return NULL;
        int l = countDepth(root->left);
        int r = countDepth(root->right);
        if(l == r)
            return root;
        else if(l < r)
            return lcaDeepestLeaves(root->right);
        else
            return lcaDeepestLeaves(root->left);
    }
    
    int countDepth(TreeNode* root){
        if(!root)
            return 0;
        if(!depth.count(root))
            depth[root] = 1 + max(countDepth(root->left), countDepth(root->right));
        return depth[root];
		
	private:
		unordered_map<TreeNode*, int> depth;
    }
};
