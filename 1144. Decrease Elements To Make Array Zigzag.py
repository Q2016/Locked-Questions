Question:
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:
Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.    
    
    
    
    
    
    
    

    
Solution: Brute-force   

Approach 1: manipulating array    
    
    
class Solution:
    
    def MovesToMakeZigZag(A):
        n=len(A)
        B=A.copy()
        
        for i in range(n):
            if i+1<n: #Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
                if i%2==0
                    if A[i]<=A[i+1]:
                        diff=A[i+1]-A[i]
                        even+=diff+1
                        A[i+1]=A[i+1]-(diff+1)
                else:
                    if A[i]>=A[i+1]:
                        diff=A[i]-A[i+1]
                        even+=diff+1
                        A[i]=A[i]-(diff+1)
        for i in range(n):
            if i+1<n: #every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
                if i%2==0
                    if B[i]<=B[i+1]:
                        diff=B[i+1]-B[i]
                        even+=diff+1
                        B[i+1]=B[i+1]-(diff+1)
                else:
                        if B[i]>=B[i+1]:
                        diff=B[i]-B[i+1]
                        even+=diff+1
                        B[i]=B[i]-(diff+1)           
    
        return min(even, odd)
    

Complexity
Time O(N) for one pass
Space O(N) for two options


Approach 2:
    
public class Solution {
    public int MovesToMakeZigzag(int[] A) {
        int n = A.Length;
        int even = 0;
        int odd = 0;        
        int first = -1;
        int second = -1;
        for(int i=0;i<n;i++)
        {
            if(i+1<n)
            {   
                if(first==-1 && second ==-1)
                {
                    first = A[i];
                    second = A[i+1];
                }
                else
                {
                    second = A[i+1];
                }
                if(i%2==0)
                {
                    if(first<=second)
                    {
                        int diff = second-first;
                        even += diff+1;
                        second = second - (diff+1);
                    }
                }
                else
                {
                    if(first>=second)
                    {
                        int diff = first-second;
                        even += diff+1;
                        first = first - (diff+1);
                    }
                } 
            }
            first = second;
        }
        //Console.WriteLine(string.Join(" ",A));
        //odd
        first = -1;
        second = -1;
        for(int i=0;i<n;i++)
        {
            if(i+1<n)
            {
                if(first==-1 && second ==-1)
                {
                    first = A[i];
                    second = A[i+1];
                }
                else
                {
                    second = A[i+1];
                }
                if(i%2==0)
                {
                    if(first>=second)
                    {
                        int diff = first-second;
                        odd += diff+1;
                        first = first - (diff+1);
                    }                    
                }
                else
                {
                    if(first<=second)
                    {
                        int diff = second-first;
                        odd += diff+1;
                        second = second - (diff+1);
                    }
                }
            }
            first = second;
        }
        //Console.WriteLine(string.Join(" ",B));
        return Math.Min(even,odd);
    }
        
    
Complexity
Time O(N) for one pass
Space O(1) for two options

