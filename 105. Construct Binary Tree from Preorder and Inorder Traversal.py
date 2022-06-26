Question:
Construct Binary Tree from Preorder and Inorder Traversal "arrays"   

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]













Solution: Recursion
    
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/  
    
Intuition

The two key observations are:

-Preorder traversal follows Root -> Left -> Right, therefore, given the preorder array preorder, 
we have easy access to the root which is preorder[0].

-Inorder traversal follows Left -> Root -> Right, therefore if we know the position of Root, we 
can recursively split the entire array into two subtrees.
    
Now the idea should be clear enough. We will design a recursion function: it will set the first 
element of preorder as the root, and then construct the entire tree. To find the left and right subtrees, 
it will look for the root in inorder, so that everything on the left should be the left subtree, and 
everything on the right should be the right subtree. Both subtrees can be constructed by making another recursion call.

It is worth noting that, while we recursively construct the subtrees, we should choose the next element 
in preorder to initialize as the new roots. This is because the current one has already been initialized 
to a parent node for the subtrees.    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)
    
    
Another solution from StefanPochmann:

Explanation/Discussion:

Consider this input:

preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]
The obvious way to build the tree is:

Use the first element of preorder, the 1, as root.
Search it in inorder.
Split inorder by it, here into [4, 2, 5] and [6, 3].
Split the rest of preorder into two parts as large as the inorder parts, here into [2, 4, 5] and [3, 6].
Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
Use preorder =[3, 6]andinorder = [6, 3] to add the right subtree.
But consider the worst case for this: A tree that's not balanced but is just a straight line to the left. Then inorder is the reverse of preorder, 
and already the cost of step 2, searching in inorder, is O(n^2) overall. Also, depending on how you "split" the arrays, you're 
looking at O(n^2) runtime and possibly O(n^2) space for that as well.

You can bring the runtime for searching down to O(n) by building a map from value to index before you start the main work, and 
I've seen several solutions do that. But that is O(n) additional space, and also the splitting problems remain. To fix those, you can 
use pointers into preorder and inorder instead of splitting them. And when you're doing that, you don't need the value-to-index map, either.

Consider the example again. Instead of finding the 1 in inorder, splitting the arrays into parts and recursing on them, just recurse on 
the full remaining arrays and stop when you come across the 1 in inorder. That's what my above solution does. Each recursive call gets told 
where to stop, and it tells its subcalls where to stop. It gives its own root value as stopper to its left subcall and its parent`s stopper 
as stopper to its right subcall.

Language details:

Small trick in my Javascript solution: The top-most call doesn't explicitly get a stopper value, so its stop is undefined. Which is good, because 
that's also what inorder[i] is when we have consumed all values, i.e., when i is inorder.length.

About the Python solution: I'm not sure there's a good way to have those p and i pointers that I use in my Javascript solution, so instead I 
opted for popping elements from preorder and inorder. Since popping from the front with pop(0) is expensive O(n), I reverse them before I 
start so I can use the cheap O(1) popping from the back.

def buildTree(self, preorder, inorder):
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)

Simple O(n) without map
