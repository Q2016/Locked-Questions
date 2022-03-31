Question:
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:
Input: nums = [[1, 2, 3],
	       [4, 5, 6],
	       [7, 8, 9]]
Output: [1,4,2,7,5,3,8,6,9]	
	
	
	
	
	
	
	
Solution: Dictionary	

https://leetcode.com/problems/diagonal-traverse-ii/discuss/597980/Python-Two-simple-solutions-(dictionary-or-sort)-O(n)

The first solution is to use dictionary. Complexity O(n)
Record the (r+c) as the key, then reverse list for each (r+c) and append it to the result.

Python:
Time O(A), Space O(A) # Two loops but they call it O(N)

Python:

    def findDiagonalOrder(self, A):
        res = []
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)
        return [a for r in res for a in reversed(r)] # What a beautiful way to flatten 2D array into 1D array

C++:
	
vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        vector<int> answer;
        unordered_map<int, vector<int>> m;
        int maxKey = 0; // maximum key inserted into the map i.e. max value of i+j indices.
        
        for (int i=0; i<nums.size(); i++) {
            for (int j=0; j<nums[i].size(); j++) {
                m[i+j].push_back(nums[i][j]); // insert nums[i][j] in bucket (i+j).
                maxKey = max(maxKey, i+j); // 
            }
        }
        for (int i=0; i<= maxKey; i++) { // Each diagonal starting with sum 0 to sum maxKey.
            for (auto x = m[i].rbegin(); x != m[i].rend(); x++) { // print in reverse order.
                answer.push_back(*x); 
            }
        }
        
        return answer;
    }	
