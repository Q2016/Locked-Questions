Question:
You are given an array of n strings strs, all of the same length. We may choose any deletion indices, and we delete all the characters in those 
indices for each string. For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions 
is ["bef", "vyz"]. Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic 
order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). 
Return the minimum possible value of answer.length.	
	
Example 1:
Input: strs = ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.	
	
	
	
	
	
	
	
	
	
Solution: brute force (difficault question)
	
We analyze words one-by-one. If in a word i a character j breaks the lexicographic order (A[i - 1][j] > A[i][j]), we add j column to the 
list of deleted columns (I am using a hash set for O(1) operations).

After we deleted a column, we need to restart the process from the beginning. The reason is that we a deleted column can break the lexicographic 
order for words we already analyzed. Note that now we ignore all columns that are already in the "deleted" list.

C++
int minDeletionSize(vector<string>& A) {
    unordered_set<int> di;
    for (auto i = 1; i < A.size(); ++i) {
        for (auto j = 0; j < A[i].size(); ++j) {
            if (di.count(j) > 0 || A[i - 1][j] == A[i][j]) continue;
            if (A[i - 1][j] > A[i][j]) {
                di.insert(j);
                i = 0;
            }
            break;
        }
    }
    return di.size();
}


Time complexity: O(N^2)
