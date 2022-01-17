class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        if(root==NULL)
            return NULL;
        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);
        
        if(root->left == NULL && root->right == NULL && root->val == target)
            return NULL;
        return root;
    }
};


/*
Iterate the tree in postorder manner and whenever we reach a leaf node, checks if its same as target, if yes then return NULL i.e. delete this leaf node. Do update the left and right subtrees returned.

Analysis :

Time complexity : O(N) ,where N is the number of nodes
Space complexity : O(h), the height of the tree is the max level the recursion can go! In worst case it can be O(N).

class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        if(root==NULL)
            return NULL;
        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);
        
        if(root->left == NULL && root->right == NULL && root->val == target)
            return NULL;
        return root;
    }
};
*/
