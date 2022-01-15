/*The question asks us to divide given people into two groups such that no two people in the same group dislike each other.

For ease of understanding, we can represent this problem as a graph, with people being the vertices and dislike-pairs being the edges of this graph.

We have to find out if the vertices can be divided into two sets such that there aren't any edges between vertices of the same set. A graph satisfying this condition is called a bipartite graph. For more on bipartite graphs, refer here.

We try to color the two sets of vertices, with RED and BLUE colors. In a bipartite graph, a RED vertex must be connected only with BLUE vertices and a BLUE vertex must be connected only with RED vertices. In other words, there must NOT be any edge connecting two vertices of the same color. Such an edge will be a conflict edge.

The presence of conflict edges indicate that bipartition is NOT possible.

The graph may consist of many connected components. For each connected component, we run our BFS algorithm to find conflict edges, if any. For each component, we start by coloring one vertex RED, and all it's neighbours BLUE. Then we visit the BLUE vertices and color all their neighbours as RED, and so on. During this process, if we come across any RED-RED edge or BLUE-BLUE edge, we have found a conflict edge and we immediately return false, as bipartition will not be possible.

If no conflict edges are found at the end of the algorithm, it means bipartition is possible, hence we return true.

Code for the above algorithm:
*/

#define WHITE 0
#define RED 1
#define BLUE 2

class Solution 
{
public:
    bool possibleBipartition(int N, vector<vector<int>> &edges) 
    {
        vector<vector<int>> adj(N + 1); // adjacency list for undirected graph
        vector<int> color(N + 1, WHITE); // color of each vertex in graph, initially WHITE
        vector<bool> explored(N + 1, false); // to check if each vertex has been explored exactly once
        
        // create adjacency list from given edges
        for (auto &edge: edges)
        {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        // print adjacency list (comment out before submitting)
        for (int i = 0; i <= N; ++i)
        {
            cout << "adj[" << i << "]: ";
            for (int j = 0; j < adj[i].size(); ++j)
            {
                cout << adj[i][j] << " ";
            }
            cout << "\n";
        }
        
        // queue to perform BFS over each connected component in the graph
        // while performing BFS, we check if we encounter any conflicts while
        // coloring the vertices of the graph
        // conflicts indicate that bi-partition is not possible
        queue<int> q;
        
        for (int i = 1; i <= N; ++i)
        {
            if (!explored[i])
            {
                // this component has not been colored yet
				// we color the first vertex RED and push it into the queue
                color[i] = RED;
                q.push(i);
                
                // perform BFS from vertex i
                while (!q.empty())
                {
                    int u = q.front();
                    q.pop();
                    
                    // check if u is already explored 
                    if (explored[u])
                    {
                        continue;
                    }
                    
                    explored[u] = true;
                    
                    // for each neighbor of u, execute this loop
                    for (auto v: adj[u])
                    {
                        // v is u's neighboring vertex
                        
                        // checking if there's any conflict in coloring
                        if (color[v] == color[u])
                        {
							// conflict edge found, so we return false 
							// as bi-partition will not be possible
                            return false;
                        }
                        
                        // we color v with the opposite color of u
                        if (color[u] == RED)
                        {
                            color[v] = BLUE;
                        }
                        else 
                        {
                            color[v] = RED;
                        }
                        
                        q.push(v);
                    }
                }
            }
        }
        
        // if no conflicts encountered then graph must be bipartite
        // so we return true
        
        return true;
    }
};
