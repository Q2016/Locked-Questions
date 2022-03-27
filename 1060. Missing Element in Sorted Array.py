Question:
Given a sorted array A of unique numbers, find the K-th missing number starting from the 
leftmost number of the array.

Example 1:
Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Example 2:
Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,…], hence the third missing number is 8.


 
  
Solution: Binary search (Check I think this problem is to be solved with Cyclic sort?)
 
Seeing the word "sorted" reminds me that there must be some trick to play with. One common thought 
of mine is binary lookup, which is used for quickly, in O(logN), to locate a specific element. And 
it turns out similar thoughts applies to this problem as well.

Before getting to that, let me explain the brute force way a little bit. First I need to set a counter 
to count missing number I find as of now, in the beginning, it will be 0 for sure. Then I can certainly 
iterate the numbers one by one, the moment I get to index i, I will check if A[i] is the last element, 
if yes, then the missing number is A[i] + (K-counter); if there is a A[i+1], then A[i+1] - A[i] - 1 is 
the number of missing numbers, for example,  between 4 and 5, there is 5-4-1=0 missing numbers while 
between 4 and 7, there is 7-4-1=2 missing (which is 5,6). Note that there is actually a clarification 
to make if [1,2] and K=3, should I return 5 or None. Here I just follow what Leetcode's submission check says.

Now let me roll my sleeves to binary lookup solution. In first iteration of binary lookup, I will get 
the missing numbers for the first and second half of the input. For example [5,7,9,10,13],  I want to 
know how many numbers are missing from the first half ([5,7,9]) and second ([9,10,13]). The way to get 
it is using the right boundry - the left  + 1, for [5,7,9], the expected numbers = 9-5+1=5, that's very 
true since a complete list  should be [5,6,7,8,9], the atual length is 3, so the missing number is 5-3=2. 
Now if I'm asked to find the 3rd missing element, I should drop the first half [5,7,9] because in that part 
there is only 2 missing. And the next step will be looking into the second half [9,10,13] for the first 
missing element since I need to find the 3rd and the first half already contain the first 2 
(which I don't really need to know what are the exact missing elements). Hmm, now I turn the search for 
 the 3rd missing in [5,7,9,10,13] into the search for the 1st missing in [9,10,13].

Repeat the process, I will know there should be 10-9+1=2 elements in [9,10] (which is the actual case so 0 missing in first half) 
 and 13-10+1=4 elements in [10,13] (which is false). So I need to look into  [10,13] for the 1st (1-0 =1) missing element.

Now since there are only 2 elements in [10,13], I will just use the left element plus the missing number 
 to get the missing number which is 10+1=11. This will be the answer!

Before I go ahead to actual code, there are still 2 tricks to mention:

There is a case that the missing number is beyond the provided array. In that condition, there is 
 no need to perform binary look. It's coverd in the brute force way and the same logic should be 
 there in the beginning in the binary lookup solution.  
In above example, I split the input array by using the middle index. In example of [5,7,9,10,13], 
 the middle index is 2 ( (4-0)/2 ). However what if the size of the array is even? Like [5,7,9,10,13,14]? 
 Since (5-0)/2 = 2.5, one may be sure what index should be used to split the array. Actually it doesn't matter. 
 The middle index could be 2 or 3 since I'm just looking for a valid index to split the array. Left half array 
 is slightly larger than right half or vice versa doesn't make an essential difference as long as the index does 
 not cross the border. And the key here is to ruduce the to-be-checked element set from a larger size to (nearly) 
 half and then (nearly) half and ....  

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:        
        def findMissingElement(left, right, newK):
            if left == right:
                return None
            if left + 1 == right:
                return nums[left] + newK
            # Python3 knowledge point 1: (0 + 3 )/2 = 1, (0 + 4) /2 =2
            middle = int((left + right) / 2)
            totalMissingNum = (nums[middle] - nums[left]) - (middle - left)
            if newK > totalMissingNum:
                return findMissingElement(middle, right, newK-totalMissingNum)
            else:
                return findMissingElement(left, middle, newK)

        numberShouldBe = (nums[-1] - nums[0] + 1) 
        numberActual   = len(nums)
        if numberShouldBe - numberActual >= k:
            return findMissingElement(0, len(nums)-1, k)
        else:
            return nums[-1] + (k - (numberShouldBe - numberActual))
            
            
Time & Space Complexity
Similar to binary lookup, each time I break the input size N to half so the time complexity will be O(logN).

In my above code, I use recursive calling which will stack to store information. This takes 
 up extra space and the space is directly related to the calls which is also O(logN). So the 
 space complexity is O(logN) as well.            
