/*
Logic is simple:

Init with root, push all nodes whose has no left or right child;
Insert new node to first node that has no left or right child.
O(1) Insert and O(nleaf) space for queue only keep nodes has no left or right child
Here is the C++ and Python code:
[C++]
*/

class CBTInserter {
private:
    queue<TreeNode*> q;
    TreeNode* head;
public:
    CBTInserter(TreeNode* root) {
        head = root;
        init_queue(root);
    }
    
    void init_queue(TreeNode* root){
        queue<TreeNode*> tq;
        tq.push(root);
        while(!tq.empty()){
            TreeNode* p = tq.front();
            tq.pop();
            if(p->left == NULL || p->right == NULL){
                q.push(p);
            }
            if(p->left != NULL){
                tq.push(p->left);
            }
            if(p->right != NULL){
                tq.push(p->right);
            }
        }
    }
    
    int insert(int v) {
        TreeNode* no = new TreeNode(v);
        TreeNode* p = q.front();
        if(p->left == NULL){
            p->left = no;
        }else{
            p->right = no;
            q.pop();
        }
        q.push(no);
        return p->val;
    }
    
    TreeNode* get_root() {
        return head;
    }
};
