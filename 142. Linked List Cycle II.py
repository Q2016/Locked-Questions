https://leetcode.com/problems/linked-list-cycle-ii/discuss/44902/Sharing-my-Python-solution


def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head
