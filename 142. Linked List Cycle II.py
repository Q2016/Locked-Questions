Question:
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
Do not modify the linked list. Follow up: Can you solve it using O(1) (i.e. constant) memory?



Solution: ---
    
https://leetcode.com/problems/linked-list-cycle-ii/discuss/44902/Sharing-my-Python-solution

Python:    
    
def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow: # we do another cycle to find the node
        slow = slow.next
        head = head.next
    return head


C++:
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(!head) return NULL;
        
        ListNode *slow=head,*fast=head;
        
        //cycle checking
        do{
            //move slow by one
            slow = slow->next;
            if(!slow) break;
            
            //move fast by 2
            fast= fast->next;
            if(!fast) break;
            fast = fast->next;
            if(!fast) break;            
            
        }while(slow!=fast);
        //no cycle
        if(!slow or !fast)
            return NULL;
        
        //check the entry point
        fast = head;
        while(fast !=slow)
            fast=fast->next, slow=slow->next;
        return fast;
    }
};    
