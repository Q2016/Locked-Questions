class Solution {
public:
    unordered_map<int, vector<TreeNode*>> cache;
    
    vector<TreeNode*> allPossibleFBT(int N) {
        vector<TreeNode*> res;
        if(cache[N].size() != 0) return cache[N];
        if(N == 1) {
            res.push_back(new TreeNode(0));
        } else {
            for (int i = 1; i < N; i += 2) {
                int l = i, r = N - i - 1;
                for (TreeNode* left : allPossibleFBT(l)) {
                    for (TreeNode* right : allPossibleFBT(r)) {
                        TreeNode * root = new TreeNode(0);
                        root->left = left;
                        root->right = right;
                        res.push_back(root);
                    }
                }
            }
        }
        cache[N] = res;
        return res;
    }
};




/*
Intuition and Algorithm

Let FBT(N) be the list of all possible full binary trees with NN nodes.

Every full binary tree TT with 3 or more nodes, has 2 children at its root. Each of those children left and right are themselves full binary trees.

Thus, for  3N≥3, we can formulate the recursion: FBT(N)= [All trees with left child from FBT(x) and right child from FBT(N−1−x), for all x].

    unordered_map<int, vector<TreeNode*>> cache;
    vector<TreeNode*> allPossibleFBT(int N) {
        vector<TreeNode*> res;
        if(cache[N].size() != 0) return cache[N];
        if(N == 1) {
            res.push_back(new TreeNode(0));
        } else {
            for (int i = 1; i < N; i += 2) {
                int l = i, r = N - i - 1;
                for (TreeNode* left : allPossibleFBT(l)) {
                    for (TreeNode* right : allPossibleFBT(r)) {
                        TreeNode * root = new TreeNode(0);
                        root->left = left;
                        root->right = right;
                        res.push_back(root);
                    }
                }
            }
        }
        cache[N] = res;
        return res;
    }
    
 */  
