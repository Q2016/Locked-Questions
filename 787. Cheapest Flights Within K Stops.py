class Solution
{
public:
    
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K)
    {        
        vector<vector<int>> dp(K+2, vector<int>(n, INT_MAX));
        
        //dp[i][j] = Distance to reach j using atmost i edges from src
        
        for(int i = 0; i <= K+1; i++)
        {
            dp[i][src] = 0; // Dist to reach src always zero
        }
        
        for(int i = 1; i <= K+1; i++)
        {
            for(auto &f: flights)
            {
                //Using indegree
                int u = f[0];
                int v = f[1];
                int w = f[2];
                
                if(dp[i-1][u] != INT_MAX)
                    dp[i][v] = min(dp[i][v], dp[i-1][u] + w);
            }
        }
        
        return (dp[K+1][dst] == INT_MAX)? -1: dp[K+1][dst];
    }
};

/*
A simple solution is to start from u, go to all adjacent vertices and recur for adjacent vertices with k as k-1, source as adjacent vertex and destination as v.

but we can optimise it by using dynamic programming approach.

DP EXPLANATION MEMORY EFFICEINT

Actually Bellman Ford is a space optimized version of 2D Dynamic Programming Solution.

To understand Bellman Ford you need to understand the 2D version first.

dp[v, k] = Shortest path from src to v using atmost k edges

dp[v, k] = {Minimum distance over all u belonging to all vertices which are coming towards v(in the indegree[v])} min(dp[u, k-1] + w(u->v)).
dp[u, k-1] becoz we have to reach to u using atmost k-1 edges. As we have to reach v using atmost k edges.

Similarly dp[u, k-1] = (p belongs to indegree[u]) min(dp[p, k-2] + w(p->u)).

Why doesn't Space optimized version work for atmost K edges case?

image

Using above example.

The space optimized version will depend on order of visiting the edges.

Suppose the order in which we relax edges is:
0->1
1->2
0->2

So after 1 round of relaxation

Distances will be 0->1 = 100
0->2 = 200
Which is wrong as using atmost 1 edge the distance from 0->2 should be 500.
The 1D version is agnostic to the order in which we visit edges.

Note: K Stops = K + 1 edges

c++ dp code

*/
