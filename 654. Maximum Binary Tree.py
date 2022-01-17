
The idea is to use divide and conquer. Each time we create a node root for the maximum value 
in the range. Then, we split it into a left range and a right range, which are the left subtree 
and right subtree of this maximum node root.



   TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return helper(nums, 0, nums.size() - 1);
    }
    
    //max_index denotes the index of the maximum number in range [left, right]
    TreeNode* helper(vector<int>& nums, int left, int right){
        if(left>right)return NULL;
        
        int max_index = left;
        for(int i = left; i<=right; i++){
            if(nums[i] > nums[max_index])max_index = i; 
        }
        
        TreeNode* root = new TreeNode(nums[max_index]);
        root->left = helper(nums, left, max_index - 1);
        root->right = helper(nums, max_index + 1, right);
        return root;
    }
