Backtracking

https://leetcode.com/problems/beautiful-arrangement/solution/

class Solution {
public:
    int count=0;
    
   int countArrangement(int N) {
    
        if (N == 0) return 0;
        vector<int> used;
       used.resize(N+1);
        helper(N, 1, used);
        return count;
    
    }
    
    
        void helper(int N, int pos, vector<int> used) {
        if (pos > N) {
            count++;
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (used[i] == 0 && (i % pos == 0 || pos % i == 0)) {
                used[i] = 1;
                helper(N, pos + 1, used);
                used[i] = 0;
            }
        }
    }

    
    
};
