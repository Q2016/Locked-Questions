class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {        
        vector<int> result = {0,0};
        result[0] = findFirst(nums,target);
        result[1] = findLast(nums,target);
        return result; 
    }
    
    int findFirst(vector<int> nums, int target){
        
        int result = -1;
        int low = 0;
        int high = nums.size() - 1;

        while(low <= high){
            int mid = low + (high-low)/2;

            if (nums[mid] < target){
                low = mid +1;
            } else if (nums[mid] > target){
                high = mid - 1;
            } else { // nums[mid] == target
                result = mid;

                // because nothing after mid
                // can be the first occurance of target.
                //maybe mid is the first occurance , maybe not
                //so let's narrow the target for [0...mid-1] and find out
                high = mid - 1; 
   
            }
        }

        return result;
  
    }
    
    int findLast(vector<int> nums, int target){
        
        int result = -1;
        int low = 0;
        int high = nums.size() - 1;
        
        while(low <= high){
            
            int mid = low + (high-low)/2;
            
            if (nums[mid] < target){
                low = mid +1;
            } else if (nums[mid] > target){
                high = mid - 1;
            } else { // nums[mid] == target
                result = mid;
                // because nothing before mid
                // can be the last occurance of target.
                //maybe mid is the last occurance , maybe not
                //so let's narrow the target for [mid+1...high] and find                   // out
                low = mid + 1;
   
            }
        }

        return result;
    }
};

/*
The problem can be simply broken down as two binary searches for the begining and end of the range, respectively:
*/
