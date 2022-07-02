Question:
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
Implement the ProductOfNumbers class:
-ProductOfNumbers() Initializes the object with an empty stream.
-void add(int num) Appends the integer num to the stream.
-int getProduct(int k) Returns the product of the last k numbers in the current list. 

Example:
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32     



Solution: ---

Similar to prefix sum. We can record the prefix product.

Explanation
If we meet 0, the product including this 0 will always be 0. We only need to record the prefix product after it.
So I clear the A and reinitilise it as [1], where 1 is the neutral element of multiplication.
        
    def __init__(self):
        self.A = [1]

    def add(self, a):
        if a == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * a)

    def getProduct(self, k):
        if k >= len(self.A): return 0
        return self.A[-1] / self.A[-k - 1]    
    
    
    
    
Complexity
Time O(1) each
Space O(N)    
