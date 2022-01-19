https://leetcode.com/problems/sort-integers-by-the-power-value/discuss/546536/Efficient-and-Easy-to-Understand-Solution-using-Dynamic-Programming




(3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
The path value for the above values will be:-
(7 6 5 4 3 2 1 0) respectively.

class Solution {
public:

unordered_map<int, int> cnt;

int traverse(int x){
    if(cnt[x] || x == 1)
        return cnt[x] ;
    
    if(x % 2)
        cnt[x] = 1+traverse(3*x + 1);
    else
        cnt[x] = 1+traverse(x/2);
    
    return cnt[x] ;
}

int getKth(int lo, int hi, int k) {

    vector<pair<int,int>> arr;
	
    for(int i = lo; i <= hi; i++)
    {
        arr.push_back({traverse(i), i}) ;
    }
	
    sort(arr.begin(), arr.end()) ;
    return arr[k-1].second;
}
};
