Question:
Given the root of a binary tree, flatten the tree into a "linked list".    

                    1          =>   1->2->3->4->5->6
                  /   \
                2       5
              /   \       \
            3       4       6

Solution: Preorder? Postorder?



private TreeNode prev = null;

public void flatten(TreeNode root) {
    if (root == null)
        return;
    flatten(root.right);
    flatten(root.left);
    root.right = prev;
    root.left = null;
    prev = root;
}
