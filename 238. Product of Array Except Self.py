

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> fromBegin(n);
        fromBegin[0]=1;
        vector<int> fromLast(n);
        fromLast[0]=1;
        
        for(int i=1;i<n;i++){
            fromBegin[i]=fromBegin[i-1]*nums[i-1];
            fromLast[i]=fromLast[i-1]*nums[n-i];
        }
        
        vector<int> res(n);
        for(int i=0;i<n;i++){
            res[i]=fromBegin[i]*fromLast[n-1-i];
        }
        return res;
    }
};
/*
We just need to change the two vectors to two integers and note that we should do multiplying operations 
for two related elements of the results vector in each loop.

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        int fromBegin=1;
        int fromLast=1;
        vector<int> res(n,1);
        
        for(int i=0;i<n;i++){
            res[i]*=fromBegin;
            fromBegin*=nums[i];
            res[n-1-i]*=fromLast;
            fromLast*=nums[n-1-i];
        }
        return res;
    }
};

*/
