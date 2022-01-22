Question: 
Convert Sorted List to Binary Search Tree


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
