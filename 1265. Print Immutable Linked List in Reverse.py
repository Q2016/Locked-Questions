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
  
Iterative - With Stack:  
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
  
  
Recursive:
  
  class Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {
        if (head == null) {
            return;
        }
        printLinkedListInReverse(head.getNext());
        head.printValue();
    }
}
Time complexity: O(N).
Space complexity: O(N). Because of the recursive stack
  
  
Follow Up - Constant space complexity

class Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {
        int numNodesCount = getNumNodesCount(head);
        for (int i = numNodesCount; i >= 1; i--) {
            printNthNode(head, i);
        }
    }
    
    private void printNthNode(ImmutableListNode head, int index) {
        ImmutableListNode node = head;
        for (int i = 0; i < index - 1; i++) {
            node = node.getNext();
        }
        node.printValue();
    }
    
    private int getNumNodesCount(ImmutableListNode head) {
        int count = 0;
        ImmutableListNode node = head;
        while (node != null) {
            count++;
            node = node.getNext();
        }
        return count;
    }
}


Complexity Analysis
Time complexity: O(n^2)
Space complexity: O(1)
  
  
Follow Up - Linear time complexity and less than linear space complexity
Idea

Split the list to  equal-size small list. Print each part in reverse order.
Mathematical proof to use sqrt(n):
 = stack size and  = recursion depth, to minimize space do: min(k+n/k)
We can solve the equation min(k+n/k) to calculate the minimum by taking the derivative and equating it to 0.  

class Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {
        Stack<ImmutableListNode> groupHead = new Stack<>();
        Stack<ImmutableListNode> workingStack = new Stack<>();
        int len = 0;
        ImmutableListNode temp = head;
        
        while (temp != null) {
            temp = temp.getNext();
            len++;
        }
        
        int groupSize = (int)Math.sqrt(len) + 1; 
        
        temp = head; 
        
        for (int i = 0; i < groupSize; i++) {
            if (i % groupSize == 0) {
                groupHead.push(temp);
            }
            temp = temp.getNext();
        }
        
        ImmutableListNode start = null, end = null; 
        
        while (!groupHead.isEmpty()) {
            end = start;
            start = groupHead.pop();
            temp = start;
            
            while (temp != end) {
                workingStack.push(temp);
                temp = temp.getNext();
            }
            
            while (!workingStack.isEmpty()) {
                workingStack.pop().printValue();
            }
        }
    }
}


Complexity Analysis
Time complexity: O(n)
Space complexity: O(sqrt(n))
