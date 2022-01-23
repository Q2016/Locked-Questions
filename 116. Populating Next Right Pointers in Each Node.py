Question:
You are given a perfect binary tree. The binary tree has the following definition:
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL    

Example:
                1                        1----->null                       
              /   \                    /   \
           2        3               2 -----> 3 ----->null
         /  \      /  \           /  \      /  \
       4     5    6    7        4 ---->5-->6---->7---->null

    


Solution: BFS

Standard BFS with mantaining pre_level and pre_node as the previous node in BFS sequence
level == pre_level means current node is not the first node of level, then pre_node.next = node and update pre_node = node
else means pre_level < level and node is the first node of level, then no need to update pre_node.next, leave it as None, update pre_node = node only.
standard BFS, append node.left and node.right to the queue
Time  Complexity: O(N)
Space Complexity: O(N)

    class Solution(object):
def connect(self, root):
    if root is None: return None
    dq, pre_level, pre_node = deque([(1, root)]), 0, None
    while dq:
        level, node = dq.popleft()
        if level == pre_level:  # current node is not the first node of level
            pre_node.next = node
            pre_node = node
        else:  # pre_level < level and node is the first node of level, then no need to update pre_node.next, 
            # leave it as None, update pre_node = node only.
            pre_level, pre_node = level, node
        if node.left:  # root is a perfect binary tree, once left exists, right must also exist
            dq.append((level + 1, node.left))
            dq.append((level + 1, node.right))
    return root
