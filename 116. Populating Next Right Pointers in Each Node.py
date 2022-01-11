class Solution {
public:
    Node* connect(Node* root) {
        if(!root)return root;
        queue<Node*> Q;
        Q.push(root);
        while(!Q.empty()){
            int n=Q.size();
            for(int i=0;i<n;i++){
                Node* x=Q.front();
                Q.pop();
                if(i!=n-1)x->next=Q.front();
                if(x->left)Q.push(x->left);
                if(x->right)Q.push(x->right);
            }
        }
        return root;
    }
};

//Iterative BFS approach using Queue
//Level Order Traversal
//T = O(n) & S = O(n) where n is total number of nodes
