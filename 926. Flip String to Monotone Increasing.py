class Solution {
public:
    int minFlipsMonoIncr(string S, int res = INT_MAX) {
        vector<int> f0(S.size() + 1), f1(S.size() + 1);
        for (int i = 1, j = S.size() - 1; j >= 0; ++i, --j) {
            f0[i] += f0[i - 1] + (S[i - 1] == '0' ? 0 : 1);
            f1[j] += f1[j + 1] + (S[j] == '1' ? 0 : 1);
        }
        for (int i = 0; i <= S.size(); ++i) res = min(res, f0[i] + f1[i]);
        return res;
    }   
};

/*We need to split the array into left '0' and right '1' sub-arrays, so that sum of '1' -> '0' flips (left) and '0' -> '1' flips (right) is minimal.

Count of '0' -> '1' flips going left to right, and store it in f0.
Count of '1' -> '0' flips going right to left, and store it in f1.
Find a the smallest f0[i] + f1[i].

    
    This reminds me of 122. Best Time to Buy and Sell Stock III. That problem has a DP solution with O(1) memory complexity, so we can try to apply it here. We can go left to right, and virtually 'move' the split point every time we see that we need less '0' -> '1' than '1' -> '0' flips (f1 = min(f0, f1 + 1 - (c - '0'))).

int minFlipsMonoIncr(string S, int f0 = 0, int f1 = 0) {
    for (auto c : S) {
        f0 += c - '0';
        f1 = min(f0, f1 + 1 - (c - '0'));
    }
    return f1;
}
*/
