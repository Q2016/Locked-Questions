standard queue level order traversal.

tmp_sum records sum of current level, global_sum records largest level sum so far.

If tmp_sum > global_sum, it means sum of current level is large, assign current level to res.

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        if (root == NULL) return 0;
        int res = 0, level = 0, global_sum = 0;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int count = q.size(), tmp_sum = 0;
            while (count--) {
                TreeNode* tmp = q.front();
                q.pop();
                tmp_sum += tmp->val;
                if (tmp->left) q.push(tmp->left);
                if (tmp->right) q.push(tmp->right);
            }
            level++;
            if (tmp_sum > global_sum) res = level;
            global_sum = max(tmp_sum, global_sum);
        }
        return res;
    }
};
