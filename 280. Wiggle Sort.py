Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

the pattern is number in odd position is peak.
First try to solve it without in-place:
Solve it in-place.
  
  
  
  
  
sort the array in increasing order.
create a result array of the same size.
keep 2 pointers, one from the beginning, one from the middle(notice odd/even of array).
put beginning first, then the middle pointer, into the result array.


# Time:  O(n)
# Space: O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or (not (i % 2) and nums[i - 1] < nums[i]):
                # Swap unordered elements.
                nums[i - 1], nums[i] = nums[i], nums[i - 1]

                
                
First try to solve it without in-place:

sort the array in increasing order.
create a result array of the same size.
keep 2 pointers, one from the beginning, one from the middle(notice odd/even of array).
put beginning first, then the middle pointer, into the result array.
Solve it in-place.

public class Solution {
    public void wiggleSort(int[] nums) {
        if(nums.length<2)  return;

        Arrays.sort(nums);
        int i=2;
        for( ; i< nums.length-1 ; ) {
            int x = nums[i];
            nums[i] = nums[i+1];
            nums[i+1] = x;
            i +=2;
        }       
    }
}
Is it really necessarily to sort the array initially ?
--NO--
noticing that the property of wiggle array is:

  if i%2 == 1, nums[i] >= nums[i-1];
  if i%2 == 0, nums[i] <= nums[i-1];
if the property is not observed, simple swap the property-break number. the previous relation at i-2 will still stand.

public class Solution {
    public void wiggleSort(int[] nums) {
        for(int i=1; i< nums.length;i++){
            if((i&1) == 1 && nums[i] < nums[i-1] 
                || (i&1) == 0 && nums[i] > nums[i-1]){
                int t = nums[i];
                nums[i] = nums[i-1];
                nums[i-1] = t;
            }
        }
    }
}                
