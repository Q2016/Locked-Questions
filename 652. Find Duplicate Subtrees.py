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

    
    
    
    
    
    
    
    
    
    
No link    
        
Solution: Postorder traversal     (post-order makes sense because we build tree bottom-up) 
  read below link:
  
  https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis
    

First the basic version, which is O(n^2) time and gets accepted in about 150 ms:

def findDuplicateSubtrees(self, root):
    def tuplify(root):
        if root:
            tuple = root.val, tuplify(root.left), tuplify(root.right)
            trees[tuple].append(root)
            return tuple
    trees = collections.defaultdict(list)
    tuplify(root)
    return [roots[0] for roots in trees.values() if roots[1:]]
  
I convert the entire tree of nested TreeNodes to a tree of nested tuples. Those have the advantage that they already support hashing and 
deep comparison (for the very unlikely cases of hash collisions). So then I can just use each subtree's tuple version as a key in my dictionary. 
And equal subtrees have the same key and thus get collected in the same list.

Overall this costs only O(n) memory (where n is the number of nodes in the given tree). The string serialization I've seen in other posted solutions 
costs O(n^2) memory (and thus also at least that much time).


So far only O(n^2) time
Unfortunately, tuples don't cache their own hash value (see this for a reason). So if I use a tuple as key and thus it gets asked for its hash value, 
it will compute it again. Which entails asking its content elements for their hashes. And if they're tuples, then they'll do the same and ask their 
elements for their hashes. And so on. So asking a tuple tree root for its hash traverses the entire tree. Which makes the above solution only 
O(n^2) time, as the following test demonstrates. It tests linear trees, and doubling the height quadruples the run time, exactly what's expected from 
a quadratic time algorithm.   
