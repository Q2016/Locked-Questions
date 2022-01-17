class Solution {
public:
    int findBestValue(vector<int>& arr, int target) {
        int sum = 0;
        int temp = -10000000;
        for (int a : arr) {
            sum += a;
            temp = max(temp, a);
        }
        if (sum == target) return temp;//max
        int min = 0; 
        int res = 1;
        int diff = 10000000;
        // The answer would lie between 0 and maximum value in the array.
        while (min <= temp) {
            int mid = min + (temp - min) / 2;
            sum = getMutatedSum(arr, mid); 
            if (sum > target) {
                temp = mid - 1;
            } else {
                min = mid + 1;
            }
            // If current difference is less than diff || current 
            //difference==diff but mid < res.(choose the smaller one.)
            if (abs(sum - target) < diff || (abs(sum - target) == diff && mid < res)) { 
                res = mid;
                diff = abs(sum - target);
            }
        }
        return res;
    }
