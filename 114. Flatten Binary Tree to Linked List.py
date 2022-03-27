Question:
Given the root of a binary tree, flatten the tree into a "linked list".    

                    1          =>   1->2->3->4->5->6
                  /   \
                2       5
              /   \       \
            3       4       6

Solution: Postorder


Great solution of the post order traversal in (right, left, root) order!
Basically, the traversing order after flattening is pre order traversal in (root, left, right), like
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
from the original tree:

    1
   / \
  2   5
 / \   \
3   4   6
If we traverse the flattened tree in the reverse way, we would notice that [6->5->4->3->2->1] is in (right, left, root) order of the original tree. 
So the reverse order after flattening is post order traversal in (right, left, root) order like [6->5->4->3->2->1].

The idea is to traverse the original tree in this order by

public void flatten(TreeNode root) {
    if (root == null)
        return;
    flatten(root.right);
    flatten(root.left);
}
and then set each node's right pointer as the previous one in [6->5->4->3->2->1], as such the right pointer behaves similar to a link in 
the flattened tree(though technically, it's still a right child reference from the tree data structure's perspective) and set the left 
child as null before the end of one recursion by

private TreeNode prev = null;

public void flatten(TreeNode root) {
    if (root == null)
        return;
    flatten(root.right);
    flatten(root.left);
    # if you check on paper below lines run for [6,5,4,3,2,1]
    # These line are similar to the lines for reverse a link list: That's acually what it does
    root.right = prev;
    root.left = null;
    prev = root;
}
