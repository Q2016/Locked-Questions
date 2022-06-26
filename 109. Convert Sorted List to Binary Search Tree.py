Question: 
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never 
differ by more than 1.

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.












Solution: Recursive

Solution 1: Convert linked list to array then do PreOrder Traversal

Convert linked list to array, then the problem become 108. Convert Sorted Array to Binary Search Tree
Choose arr[mid] as a root
Solve sub problem (left, mid - 1), make it as left node
Solve sub problem (mid + 1, right), make it as right node


class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        List<Integer> arr = new ArrayList<>();
        while (head != null) {
            arr.add(head.val);
            head = head.next;
        }
        return buildBST(arr, 0, arr.size() - 1);
    }
    TreeNode buildBST(List<Integer> list, int left, int right) {
        if (left > right) return null;
        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(list.get(mid));
        root.left = buildBST(list, left, mid - 1);
        root.right = buildBST(list, mid + 1, right);
        return root;
    }
}



operate linked-list directly

# recursively
def sortedListToBST(self, head):
    if not head:
        return 
    if not head.next:
        return TreeNode(head.val)
    
    # here we get the middle point,
    # even case, like '1234', slow points to '2',
    # '3' is root, '12' belongs to left, '4' is right
    # odd case, like '12345', slow points to '2', '12'
    # belongs to left, '3' is root, '45' belongs to right
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # tmp points to root
    tmp = slow.next
    # cut down the left child
    slow.next = None
    
    root = TreeNode(tmp.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(tmp.next)
    return root
