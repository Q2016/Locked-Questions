https://ttzztt.gitbooks.io/lc/content/linked-list/insert-into-a-cyclic-sorted-list.html

Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to_any_single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node isnull), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.

Thoughts:

No head:
prev.val <= val <= cur.val
prev.val > cur.val and (val < cur.val or prev.val < cur): cur is either the min or the max with not all nodes with the same value
val != every nodes's value in a cyclic linked list where every node has the same value


class Solution(object):
    def insert(self, head, val):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        node = Node(val, head)
        # case 1 no head
        if not head:
            return node
        prev, cur = head, head.next
        while 1:
            # case 2: prev.val <= val <= cur.val
            if prev.val <= val <= cur.val:
                break

            # case 3: prev.val > cur.val and val < cur.val or prev.val < cur
            elif prev.val > cur.val and (val <= cur.val or prev.val <= val):
                break

            prev, cur = prev.next, cur.next
            # case 4: prev == head
            if prev == head: # in case of all nodes have same value that are > val 
                break

        # insert node between prev and cur
        prev.next = node
        node.next = cur

        return head
