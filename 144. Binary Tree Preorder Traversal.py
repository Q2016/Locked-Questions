Question:
Given the root of a binary tree, return the preorder traversal of its nodes' values.    

Solution: Recursive or iterative

# recursively
def preorderTraversal1(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
