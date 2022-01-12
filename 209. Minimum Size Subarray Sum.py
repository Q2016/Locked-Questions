//sliding window


class Solution {
public:
    int minSubArrayLen(int s, vector<int>& A) {
        int i = 0, n = A.size(), res = n + 1;
        for (int j = 0; j < n; ++j) {
            s -= A[j];
            while (s <= 0) {
                res = min(res, j - i + 1);
                s += A[i++];
            }
        }
        return res % (n + 1);
    }
};

/*
Intuition
Shortest Subarray with Sum at Least K
Actually I did this first, the same prolem but have negatives.
I suggest solving this prolem first then take 862 as a follow-up.

Explanation
The result is initialized as res = n + 1.
One pass, remove the value from sum s by doing s -= A[j].
If s <= 0, it means the total sum of A[i] + ... + A[j] >= sum that we want.
Then we update the res = min(res, j - i + 1)
Finally we return the result res
*/




//Complexity
//Time O(N)
//Space O(1)
