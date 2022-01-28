Question:
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example: Given binary tree
          1
         / \
        2   3
       / \     
      4   5
Returns [4, 5, 3], [2], [1].


Solution: DFS

    def findLeaves(self, root):

        def findLeavesHelper(node, result):
            if not node:
                return -1
            level = 1 + max(findLeavesHelper(node.left, result), findLeavesHelper(node.right, result))
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            return level

        result = []
        findLeavesHelper(root, result)
        return result


# Time:  O(n)
# Space: O(h)
