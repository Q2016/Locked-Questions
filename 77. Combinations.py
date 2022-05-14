Question:
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n. 
For example,
If n = 4 and k = 2, a solution is: [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]


    
    
    
    
    
    
    
    
    
    
    
Solution: Backtracking
     
Template first.
All those combination problems share a common characteristic: either select the element at current position or not, and continue the same 
process to the next position. Therefore, I summarized a simple template to those problems.

vector<vector<int>> main(...){
    vector<vector<int>>res;  // Store the result, could be other container
    backtrack(res, ...);  // Recursion function to fill the res
    return res;
}

void backtrack(vector<vector<int>>& res, int cur, ..., vector<int>vec){
    if(meet the end critria, i.e. cur reach the end of array){  
        //vec could be a certain path/combination/subset
        res.push_back(vec);
        return;
    }
    // Current element is not selected
    backtrack(res, cur+1, ..., vec);
    // Current element is selected
    vec.push_back(cur); // or could be vec.push_back(nums[cur]), vec.push_back(graph[cur]);
    backtrack(res,cur+1, ..., vec);
}
Now go back to this problem(LeetCode 77. Combinations), we are asked to return all possible combinations of k numbers out of 1 ... n.
We start from 1, if 1 is selected, k = k-1; if 1 is not selected, k = k; proceed to next number, until k becomes 0 - the end critria.
Code:

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>>res;
        backtrack(res,1,n,k,vector<int>());
        return res;
    }
    
    void backtrack(vector<vector<int>>& res, int cur, int n, int k, vector<int>comb){
        if(k==0){
            res.push_back(comb);
            return;
        }
        // If cur>n-k, there are not enough numbers left, we have to select the current element
        if(cur<=n-k) backtrack(res,cur+1,n,k,comb);  
        comb.push_back(cur);
        backtrack(res,cur+1,n,k-1,comb);
    }
Or start with number n, and decreasing.

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>>res;
        backtrack(res,n,k,vector<int>());
        return res;
    }
    
    void backtrack(vector<vector<int>>& res, int n, int k, vector<int>comb){
        if(k==0){
            res.push_back(comb);
            return;
        }
        if(n>k) backtrack(res,n-1,k,comb);
        comb.push_back(n);
        backtrack(res,n-1,k-1,comb);
    }
Here is another combination problem, LeetCode 78. Subsets: Given a set of distinct integers, nums, return all possible subsets.
We can use this template as well, pretty much the same code.

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>res;
        backtrack(nums,0,vector<int>(),res);
        return res;
    }
    
    void backtrack(vector<int>& nums, int k,vector<int>subset,vector<vector<int>>& res){
        if(k==nums.size()){
            res.push_back(subset);
            return;
        }
        backtrack(nums,k+1,subset,res);
        subset.push_back(nums[k]);
        backtrack(nums,k+1,subset,res);
    }
Still, I think the template may have room to improve, it costs too much memory.
One way to solve it is to change vector<int>vec to vector<int>&vec, and add vec.pop_back() at the end of backtrack(), but it may increase 
the time complexity, don't know which one is better.

EDIT(8/1/2017): Just found another combination problem, LeetCode 93. Restore IP Addresses: Given a string containing only digits, restore it 
by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"].

Can be easily solved using template:

    vector<string> restoreIpAddresses(string s) {
        vector<string> res;
        backtrack(res, s, 0, "", 0);
        return res;
    }
    
    void backtrack(vector<string>& res, string s, int pos, string comb, int num){
        if(num > 4) return;  // IP address only allows for 4 segments
        if(pos >= s.size()){
            if(num == 4){
                comb.pop_back();
                res.push_back(comb);
            }
            return;
        }
        // 3 digit
        if(s[pos] != '0' && pos < s.size()-2 && stoi(s.substr(pos,3)) < 256)
            backtrack(res, s, pos + 3, comb + s.substr(pos,3) + ".", num + 1);
        // 2 digit
        if(s[pos] != '0' && pos < s.size()-1)
            backtrack(res, s, pos + 2, comb + s.substr(pos,2) + ".", num + 1);
        // 1 digit
        backtrack(res, s, pos + 1, comb + s.substr(pos,1) + ".", num + 1);
    }
Update(8/3/2017): 131. Palindrome Partitioning : Given a string s, partition s such that every substring of the partition is a palindrome. 
Solution:

    vector<vector<string>> partition(string s) {
        vector<vector<string>>res;
        backtrack(res,s,0,vector<string>());
        return res;
    }
    
    void backtrack(vector<vector<string>>& res, string s, int pos, vector<string> comb){
        if(pos >= s.size()){
            res.push_back(comb);
            return;
        }
        // Palindrome length == 1
        comb.push_back(s.substr(pos,1));
        backtrack(res, s, pos + 1, comb);
        comb.pop_back();
        // Palindrome length > 1
        for(int step = 2; pos + step <= s.size(); step++){
            if(isPalindrome(s.substr(pos, step))){
                comb.push_back(s.substr(pos, step));
                backtrack(res, s, pos + step, comb);
                comb.pop_back();
            }
        }
    }
    
    bool isPalindrome(string s){
        int i(0), j(s.size()-1);
        while(i < j) 
            if(s[i++] != s[j--]) return false;
        return true;
    }    



    
   
