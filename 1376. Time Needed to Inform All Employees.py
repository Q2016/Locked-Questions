//We go from root (head) to all leaves (employees). Since the procedure happens in parallel 
in tree branches, we need to return the longest time from head to a leaf.



class Solution {
public:

    int dfs(int i, vector<vector<int>> &m, vector<int>& informTime, int mx = 0) {
        for (auto d : m[i])
            mx = max(mx, dfs(d, m, informTime));
        return informTime[i] + mx;
    }
    
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<vector<int>> m(n);
        for(auto i = 0; i < manager.size(); ++i)
            if (manager[i] != -1)
                m[manager[i]].push_back(i);
        return dfs(headID, m, informTime);
    }
};
