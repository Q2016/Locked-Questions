
So this can satisfy O(h) memory, hasNext() in O(1) time,
But next() is O(h) time.

I can't find a solution that can satisfy both next() in O(1) time, space in O(h)

class BSTIterator {
private:    
    stack<TreeNode*> node_stack;
public:
    BSTIterator(TreeNode *root) {
        while(root) 
        {
            node_stack.push(root);
            root = root->left;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !node_stack.empty();
    }

    /** @return the next smallest number */
    int next() {
        TreeNode *t = node_stack.top();
        node_stack.pop();
        int ret = t->val;
        t = t->right;
        while(t)
        {
            node_stack.push(t);
            t = t->left;
        }
        return ret;
    }
};
