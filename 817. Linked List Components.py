Take second example in the description:
liked list: 0->1->2->3->4
I highlighed the subset G in linked list with color red.
The problem is just to count how many red part there are.
One red part is one connected components.
To do this, we just need to count tails of red parts.



    def numComponents(self, head, G):
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res
