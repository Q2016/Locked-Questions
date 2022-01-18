https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/328119/Simple-Python-Solution%3A-top-down-DFS


Please see and vote for my solutions for these similar problems.

257. Binary Tree Paths

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, path, res):
            if node.left == None and node.right == None:
                res.append(path + str(node.val))
            if node.left:
                dfs(node.left, path + str(node.val) + '->', res)
            if node.right:
                dfs(node.right, path + str(node.val) + '->', res)
        
        if not root:
            return []
        res = []
        dfs(root, "", res)
        return res
129. Sum Root to Leaf Numbers

    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, bits, res):
            if node.left == None and node.right == None:
                res[0] += int(bits + str(node.val), 10)
            if node.left:
                dfs(node.left, bits + str(node.val), res)
            if node.right:
                dfs(node.right, bits + str(node.val), res)
        
        if root == None:
            return 0
        bits, res = '', [0]
        dfs(root, bits, res)
        return res[0]
1022. Sum of Root To Leaf Binary Numbers

    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, bits, res):
            if node.left == None and node.right == None:
                res[0] += int(bits + str(node.val), 2)
            if node.left:
                dfs(node.left, bits + str(node.val), res)
            if node.right:
                dfs(node.right, bits + str(node.val), res)
        
        if root == None:
            return 0
        bits, res = '', [0]
        dfs(root, bits, res)
        return res[0]
988. Smallest String Starting From Leaf

    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(root, s):
            s = s + chr(ord('a') + root.val)
            if not root.left and not root.right:
                if res[0] == None:
                    res[0] = s[::-1]
                else:
                    res[0] = min(res[0], s[::-1])
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
        
        if not root:
            return ''
        res = [None]
        dfs(root, '')
        return res[0]
112. Path Sum

    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        def dfs(root, curr_s):
            curr_s += root.val
            if not root.left and not root.right:
                if curr_s == s:
                    res[0] = True
                    return
            if not res[0] and root.left:
                dfs(root.left, curr_s)
            if not res[0] and root.right:
                dfs(root.right, curr_s)
        
        if not root:
            return False
        res = [False]
        dfs(root, 0)
        return res[0]
113. Path Sum II

    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        def dfs(root, lst, curr_s):
            curr_s += root.val
            if not root.left and not root.right:
                if curr_s == s:
                    res.append(lst + [root.val])
                    return
            if root.left:
                dfs(root.left, lst + [root.val], curr_s)
            if root.right:
                dfs(root.right, lst + [root.val], curr_s)
        
        if not root:
            return []
        res = []
        dfs(root, [], 0)
        return res
437. Path Sum III (Similar problem: 560. Subarray Sum Equals K)

    def pathSum(self, root, s):
        def dfs(root, curr_s):
            curr_s += root.val
            res[0] += pre_sums.get(curr_s - s, 0)
            pre_sums[curr_s] = pre_sums.get(curr_s, 0) + 1
            if root.left:
                dfs(root.left, curr_s)
            if root.right:
                dfs(root.right, curr_s)
            pre_sums[curr_s] -= 1
            if pre_sums[curr_s] == 0:
                del pre_sums[curr_s]
        
        res = [0]
        pre_sums = {0: 1}
        if not root:
            return res[0]
        dfs(root, 0)
        return res[0]
