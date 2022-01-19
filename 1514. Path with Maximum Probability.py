/*
Q & A
Q1: Why negative weights can be used in Dijkstra's algorithm here in Python 3 code? I thought it's not allowed.
A1: Excellent question, negative weight is used ONLY in heapq to order its priority by reversed weight order. In fact, when calculating Prob., we still use positive value -prob.
Q2: Why Belman Ford actually works when vertices and edges can be as large as 10000 and 20000, respectively? If algo is O(n * E) it would be at least 200 000 000 operations, which is too much.
A2: - credit to @Binga45: O(n * E) is a very loose upper bound, and the code actually prunes enough branches to make itself run fast; Specifically, the bellman ford code won't add already visited vertices in most of the scenarios as we are enforcing below condition before adding to the queue.

	if (p[cur] * succProb[index] > p[neighbor]) {
		p[neighbor] = p[cur] * succProb[index];
		q.offer(neighbor);
	}
So, let's imagine an edge v-t and the probability connecting them to be 1. We have visited vand based on probability p[v], we updated p[t] also to the same value as p[v] as the edge connecting them has a prob of 1. Now, when we add t to the queue, we won't revisit the already visited neighbor v as p[t] * 1 is not > p[v].

The only exception to the above scenario is when we have another vertex u in the same level(depth) as v with a p[u] > p[v] and probability of edge u-t is 1. Then, we will revisit v from t, because in this scenario, p[t] * 1 > p[v] as p[t] is updated by u vertex. -- credit to @Binga45

End of Q & A.

In case you are NOT familiar with Bellman Ford and Dijkstra's algorithm, the following links are excellent materials for you to learn:

Bellman Ford algorithm:
https://algs4.cs.princeton.edu/44sp/
https://algs4.cs.princeton.edu/44sp/BellmanFordSP.java.html
https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture14.pdf
https://en.wikipedia.org/wiki/Bellman–Ford_algorithm
https://www.geeks for geeks.org/bellman-ford-algorithm-dp-23/(remove the 2 spaces among the links to make it valid)

Dijkstra's algorithm:
https://algs4.cs.princeton.edu/44sp/
https://algs4.cs.princeton.edu/44sp/DijkstraSP.java.html
https://en.wikipedia.org/wiki/Dijkstra's_algorithm
https://www.geeks for geeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/ (remove the 2 spaces among the links to make it valid)
/*


Bellman Ford:

Initialize all vertices probabilities as 0, except start, which is 1;
Use BFS to traverse all reachable vertices from start, update the corresponding probilities whenever we can have a higher probability; otherwise, ignore that vertex; Note: when forwarding one step, multiply the corresponding succProb value with the probaboility of current vertex;
Repeat 2 till all probabilities reach their maximum values.
Return the probability of end as solution.
   
*/


class Solution {
public:
    
double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        //create own graph
        vector<unordered_map<int, double>> graph(n);
        for(int i = 0; i < edges.size(); ++i) {
            graph[edges[i][0]][edges[i][1]] = succProb[i];
            graph[edges[i][1]][edges[i][0]] = succProb[i];
        }
        
        //functionality wise, this array works as a visited array, 
        //only when we find a larger probability than the stored value
        //we will need to push next node into the queue
        vector<double> ps(n, 0.0);  ///probability of reaching each node
        
        ps[start] = 1.0; //important intilization
        
        queue<int> q;
        q.push(start);
        double res = 0;
        while(!q.empty()) {
            int nd = q.front();
            q.pop();
            for(auto& it: graph[nd]) {
                int next = it.first;
                double pro = it.second;
                //ok, we can reach this node with a larger probability, try starting from it
                //a node might be pushed into the queue more than once
                if(ps[nd] * pro > ps[next]) {
                    q.push(next);
                    ps[next] = ps[nd] * pro;
                }
            }
        }
        
        return ps[end];
    }
};
