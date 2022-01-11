/*
Using Heap :- Here, we know that the row and column is already sorted. Therefore, instead of traversing in the entire matrix we can take advantage of that. We can take a Min Heap and push the First row(value, indexes) into Min heap. You can push first column also, and write your answer according to that.
Now,follow these steps:-

pop the element from min heap and
check whether it is the Kth smallest element, if it is return the value,
else push the next row value (Note:- column is going to remain same).
The reason behind this logic is , when we remove the smallest element from Min Heap (i.e our 1st smallest element, which is always present in the 1st row and 1st column), then the 2nd smallest element may lie in that 2nd row and 1st column or it may be present in the First Row and column greater than 1.
Time Complexity:- O(NlogN)
Space Complexity:- O(N)
*/

class Solution {
public:
int kthSmallest(vector<vector<int>>& mat, int k) {
    priority_queue<pair<int,pair<int,int>>, vector<pair<int,pair<int,int>>>, greater<pair<int,pair<int,int>>> > pq;
    int n=mat.size();
    for(int i=0; i<n; ++i)
        pq.push({mat[0][i],{0,i}});

    int ans;
        
    while(k--){
        int val=pq.top().first;
        int row=pq.top().second.first;
        int col=pq.top().second.second;
        pq.pop();
        ans=val;
        if(row!=n-1)
            pq.push({mat[row+1][col],{row+1,col}});
    }
        return ans;
    }
};
