Question:
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.
Note: A subtree must include all of its descendants. Follow up: Can you figure out ways to solve it with O(n) time complexity?

Example:
     10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is 5. The return value is the subtree's size, which is 3.

Hint:

You can recursively use algorithm similar to 98. Validate Binary Search Tree at each 
node of the tree, which will result in O(nlogn) time complexity.


This question asks us to find the largest binary search subtree of a binary tree. 
The so-called binary search tree is a binary tree that satisfies left < root < right, 
and we need to return the number of nodes in this binary search subtree. The hint given 
in the title says that it can be done with the previous  method of Validate Binary Search Tree  , 
with a time complexity of O(n^2 ). This method treats each node as a root node to verify whether 
it is binary. Search the number and record the number of nodes. If it is a binary search tree, 
update the final result. See the code as follows:

 

Solution one:

class Solution {
 public :
     int largestBSTSubtree(TreeNode* root) {
         int res = 0 ;
        dfs(root, res);
        return res;
    }
    void dfs(TreeNode *root, int & res) {
         if (!root) return ;
         int d = countBFS(root, INT_MIN, INT_MAX);
         if (d != - 1 ) {
            res = max(res, d);
             return ;
        }
        dfs(root -> left, res);
        dfs(root -> right, res);
    }
    int countBFS(TreeNode *root, int mn, int mx) {
         if (!root) return  0 ;
         if (root->val <= mn || root->val >= mx) return - 1 ;
         int left = countBFS( root->left, mn, root-> val);
         if (left == - 1 ) return - 1 ;
         int right = countBFS(root->right, root-> val, mx);
         if (right == - 1 ) return - 1 ;
         returnleft + right + 1 ;
    }
};
 

Let's look at a more concise way of writing. For each node, verify whether it is a BST. 
If so, just count the number of nodes. See the code as follows:

 

Solution two:

class Solution {
 public :
     int largestBSTSubtree(TreeNode* root) {
         if (!root) return  0 ;
         if (isValid(root, INT_MIN, INT_MAX)) return count(root);
         return max(largestBSTSubtree(root->left), largestBSTSubtree (root-> right));
    }
    bool isValid(TreeNode* root, int mn, int mx) {
         if (!root) return  true ;
         if (root->val <= mn || root->val >= mx) return  false ;
         return isValid(root-> left, mn, root->val) && isValid(root->right, root-> val, mx);
    }
    int count(TreeNode* root) {
         if (!root) return  0 ;
         return count(root->left) + count(root->right) + 1 ;
    }
};
 

The Follow up in the title allows to solve the problem with the time complexity of O(n), 
or use the DFS idea to solve the problem. Due to the limitation of time complexity, only 
one traversal of the entire binary tree is allowed. Due to the binary search that meets 
the requirements of the title The subtree must have leaf nodes, so the idea is to first 
recurse to the leftmost child node, and then recurse layer by layer. For each node, 
record the current maximum number of BST nodes as the maximum value of the left subtree , 
and as the minimum value of the right subtree, when each encounter that the left child 
node does not exist or the current node value is greater than the maximum value of the 
left subtree, and the right subtree does not exist or the current node value is less 
than the minimum number of the right subtree If the current node is not a BST node, 
then the updated BST node number res is the larger value of the respective BST nodes 
of the left and right child nodes, see code show as below:

 

Solution three:

class Solution {
 public :
     int largestBSTSubtree(TreeNode* root) {
         int res = 0 , mn = INT_MIN, mx = INT_MAX;
        isValidBST(root, mn, mx, res);
        return res;
    }
    void isValidBST(TreeNode* root, int & mn, int & mx, int & res) {
         if (!root) return ;
         int left_cnt = 0 , right_cnt = 0 , left_mn = INT_MIN;
         int right_mn = INT_MIN, left_mx = INT_MAX, right_mx = INT_MAX;
        isValidBST(root -> left, left_mn, left_mx, left_cnt);
        isValidBST(root -> right, right_mn, right_mx, right_cnt);
         if ((!root->left || root->val > left_mx) && (!root->right || root->val < right_mn)) {
            res = left_cnt + right_cnt + 1 ;
            mn = root->left ? left_mn : root-> val;
            mx = root->right ? right_mx : root-> val;
        } else {
            res = max(left_cnt, right_cnt);    
        }
    }
};
 

The above solution defines a large number of variables in the recursive function, 
which is inevitably dazzling. We can simplify it a little and put these variables 
into the return value of the recursive function. At this time, the helper function 
returns a one-dimensional array. , there are three numbers in it, which are the 
minimum and maximum of the number of the current node as the root node, and the
maximum number of nodes in the BST subtree. Then you can count the number in the 
process of verifying the BST. First, it is judged to be empty. If it is empty, it 
will return a default triple, integer maximum value, minimum value, and 0. Then you 
may have doubts, isn't the definition saying that the first value is the minimum 
value? That's right, I'll explain it later. If the current node node exists, call 
the recursive function on its left and right child nodes respectively, then the 
information of the left subtree and the right subtree are saved in the left and 
right arrays, even if the left and right child nodes do not exist, it does not 
matter, because the first If the sentence is empty, you will still get a default 
triple. The next step is to update the result res according to the information 
of the left and right subtrees. Due to the definition of BST, the current node 
value must be greater than the maximum value of the left subtree and less than 
the minimum value of the right subtree. The maximum value of the left subtree is 
stored in left[1], and the minimum value of the right subtree is stored in 
right[0]. If these two conditions are satisfied, it means that the left and 
right subtrees are BST, then the returned triple The minimum value is the smaller 
of the current node value and the minimum value of the left subtree, the maximum 
value is the larger value of the current node value and the maximum value of the 
right subtree, and the number of returned BST nodes is the left and right subtrees 
Add 1 to the number of nodes to count the current node. Ok, now explain why the 
order of the triple returned when it is empty is the largest integer and the 
smallest integer. If it is currently a leaf node, which is also considered a BST, 
then it is definitely hoped to enter the if clause, so that the third item of the 
triplet can be added by 1, but the condition of the if is that the current node 
value is greater than the largest value in the left subtree value, now the left 
child node is empty, in order to ensure that the condition can pass, we set the 
maximum value of the empty left subtree to the minimum value of the integer, so 
that it must pass, and similarly, set the minimum value of the empty right 
subtree to the minimum value. The value is set to the maximum integer value, 
which is what triples of empty nodes do. Well, continue to look at the contents 
of else, if the rules of BST are broken, the minimum value of the returned 
triplet is the minimum value of the integer type, the maximum value is the 
maximum value of the integer type, and the number of BST nodes is not 0, because 
its There may also be BSTs in the left and right subtrees, so it is a BST in the 
left and right subtreesThe larger value in the number of nodes, see the code as follows:

 

Solution four:

class Solution {
 public :
     int largestBSTSubtree(TreeNode* root) {
        vector < int > res = helper(root);
         return res[ 2 ];
    }
    vector < int > helper(TreeNode* node) {
         if (!node) return {INT_MAX, INT_MIN, 0 };
        vector < int > left = helper(node->left), right = helper(node-> right);
         if (node->val > left[ 1 ] && node->val < right[ 0 ]) {
             return {min (node->val, left[ 0 ]), max(node->val, right[ 1 ]), left[ 2 ] + right[ 2 ] + 1 };
        } else {
             return {INT_MIN, INT_MAX, max(left[ 2 ], right[ 2 ])};
        }
    }
};



