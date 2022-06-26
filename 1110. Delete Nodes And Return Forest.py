Question:
Given the root of a binary tree, after deleting all nodes with a value in to_delete, we are left with a forest.
Return the roots of the trees in the remaining forest. 

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]








    

Solution: Recursion Preorder? (This question is very smailar to one of the easy questions?, it's also similar to 450.)

https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution

def delNodes(self, root, to_delete):
    to_delete_set = set(to_delete)
    res = []

    def helper(root, is_root):
        if not root: return None
        root_deleted = root.val in to_delete_set
        
        if is_root and not root_deleted:
            res.append(root)
        root.left = helper(root.left, root_deleted)
        root.right = helper(root.right, root_deleted)
        return None if root_deleted else root
    
    helper(root, True)
    return res

                     
                     
Complexity
Time O(N)
Space O(H + N), where H is the height of tree.                     
