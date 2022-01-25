Question:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.	


Solution:---

https://leetcode.com/problems/reorder-list/discuss/1640597/PythonJavaC%2B%2B-2-Easy-Solutions-oror-Visualized-Explanation-oror-Beginner-Friendly

step 1: find the middle pointer of the linked list and split the linked list into two halves using slow and fast pointers
head = [1, 2, 3, 4, 5]    => head = [1, 2, 3]   mid  = [4, 5]		
step 2: reverse the second half
head = [1, 2, 3]
mid  = [4, 5]             =>    mid = [5, 4]
step 3: interleaving merge the first half and the reversed second half
head = [1, 2, 3]
		   =>    head = [1, 5, 2, 4, 3]
mid = [5, 4]

Time  Complexity: O(N)
Space Complexity: O(1)
  
  
      def reorderList(self, head):
        if head.next:
            # step 1: find the middle pointer of the linked list
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None

            # step 2: reverse the last half linked list
            p, q, mid.next = mid, mid.next, None
            while q:
                p, q, p.next = q, q.next, p
            mid = p

            # step 3: merge first half and reversed last half
            p, q = head, mid
            while q:
                pp, qq = p, q  # backup p and q
                p, q = p.next, q.next
                pp.next, qq.next = qq, p
