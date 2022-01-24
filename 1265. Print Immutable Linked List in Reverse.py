Question:
You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:
ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can’t access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
You must solve this problem without modifying the linked list. 
In other words, you must operate the linked list using only the mentioned APIs.

Example 1:
Input: head = [1,2,3,4]
Output: [4,3,2,1]
  
Could you solve this problem in:
Constant space complexity?
Linear time complexity and less than linear space complexity?


Solution:  
Use a list to record LinkedList nodes and then do a reverse.


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        results = []
        while head:
            results.append(head)
            head = head.getNext()
        
        for head in results[::-1]:
            head.printValue()

Time complexity: O(N).
Space complexity: O(N).
