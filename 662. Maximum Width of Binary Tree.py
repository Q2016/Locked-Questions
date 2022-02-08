Question:
Given the root of a binary tree, return the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between 
the end-nodes are also counted into the length calculation.      1 [1,1]
                                                                / \
                                                       [2,2]   3    2 [3,2] -----> brackets are for the solution below
                                                              / \       \
Example 1:                                           [4,3]   5   3[5,3]  9 [6,3]
Input: root = [1,3,2,5,3,null,9], Output: 4, Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).    

        
Solution: BFS
In this problem we need to find maximum width of binary tree, so we need to use some tree traversal algorithm. BFS or DFS? I prefer to use BFS, 
because it emulate level by level traversal. While we traverse we need to keep some information about our node: its level, but also its num, 
which is number in level if this level was full. So, let us keep 3 informations for each node: [num, level, node]. How we change this information, 
when we traverse tree? We increase level by 1, and for num, for left children we evaluate 2*num and for the right we evaluate 2*num + 1. 
You can see how it works on the following tree (here in brackets I show 2 numbers : [num, level]. 
So, we traverse our tree, using BFS, keep this information. Also we have level_old and num_old variable, which keep information for the first 
(the most left) node on each level, using this values we can understand if new level is started, and if started, we update it and for each new 
node we can evaluate current width of traversing layer.

    def widthOfBinaryTree(self, root):
        level_old, num_old, max_width = 1, 1, 0
        queue = deque([[level_old,num_old,root]])

        while queue:    
            [num, level, node] = queue.popleft()
            if level > level_old:
                level_old, num_old = level, num
                
            max_width = max(max_width, num - num_old + 1)
            if node.left:  queue.append([num*2,  level+1, node.left])
            if node.right: queue.append([num*2+1,level+1, node.right])
                
        return max_width


Complexity: time complexity is O(n), where n is number of nodes, because we traverse our tree, using bfs. 
Space complexity is O(w), where w is the biggest number of nodes in level, because we need to keep our queue. 
Potentially it is equal to O(n). If we use DFS, then space complexity will be O(h), where h is height of tree.
