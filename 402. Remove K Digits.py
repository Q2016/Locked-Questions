Question:
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


Solution: Using stack
The first algorithm is straight-forward. Let's think about the simplest case: how to remove 1 digit from the number so 
that the new number is the smallest possible？ Well, one can simply scan from left to right, and remove the first "peak" 
digit; the peak digit is larger than its right neighbor. One can repeat this procedure k times, and obtain the first algorithm:

string removeKdigits(string num, int k) {
        while (k > 0) {
            int n = num.size();
            int i = 0;
            while (i+1<n && num[i]<=num[i+1])  i++;
            num.erase(i, 1);
            k--;
        }
        // trim leading zeros
        int s = 0;
        while (s<(int)num.size()-1 && num[s]=='0')  s++;
        num.erase(0, s);
        
        return num=="" ? "0" : num;
    }

The above algorithm is a bit inefficient because it frequently remove a particular element from a string and has complexity O(k*n).
One can simulate the above procedure by using a stack, and obtain a O(n) algorithm. Note, when the result stack (i.e. res) pop a digit, 
it is equivalent as remove that "peak" digit.


    def removeKdigits(self, num, k):

        result = []
        for d in num:
            while k and result and result[-1] > d:
                result.pop()
                k -= 1
            result.append(d)
        return ''.join(result).lstrip('0')[:-k or None] or '0'
    
    
# Time:  O(n)
# Space: O(n)    
