Question:
Given the root of a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the 
root node of any one of them. Two trees are duplicate if they have the same structure with the same node values.
                                1
                              /   \
                           --2     3
                           /     /   \
                          4   --2     4
                              /
Example 1:                   4
Input: root = [1,2,3,4,null,2,4,null,null,4], Output: [[2,4],[4]]    

        
Solution: Postorder traversal       

    def findDuplicateSubtrees(self, root):
        def postOrderTraversal(node, lookup, result):
            if not node:
                return ""
            s = "(" + postOrderTraversal(node.left, lookup, result) + str(node.val) + postOrderTraversal(node.right, lookup, result) + ")"
            if lookup[s] == 1:
                result.append(node)
            lookup[s] += 1
            return s
        lookup = collections.defaultdict(int)
        result = []
        postOrderTraversal(root, lookup, result)
        return result

    
# Time:  O(n * h)
# Space: O(n * h)    
