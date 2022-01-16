
/*
Key Idea
The base case that we know is - All outgoing edges from 0 must be reversed. So add the count into our final result.
At this stage, we can say all edges are coming into node 0. What is the next thing we need to do?
Make sure that all nodes that are connected to 0 have all edges coming into them.
E.g. if nodes x and y are connected to 0. After first step, there will be edges from x to 0 and y to 0. Now we want to make sure that all nodes that are directly connected to x, must have an edge coming into x. Similarly for y. If we keep on doing this recursively, we will get the answer at the end. Along the way, we will keep counting the edges that we reversed.

Implementation
For the ease of implementation, I have created two separate graph, one for outgoing edges and another for incoming. Everytime an edge is traversed, I erase the opposite edge so that I don’t hit the same node twice.
*/



class Solution {
public:
    unordered_map<int, unordered_set<int>> out, in;
    int ans = 0;
    
    void dfs(int node) {
        
        // Why we need to traverse both incoming as well as outgoing edges?
        // Ans. 
        // We want all edges to come towards 0. Reversing outgoing edges
        // from 0 is necessary - you can understand this easily.
        // Then you need to recursively orient all outgoing edges from 
        // those connected nodes too.
        // But why do we need to recursively call dfs() even for incoming
        // edges? 
        // The answer is, we don't know the orientation of edges that are 
        // connected to that neighbor node.
        // For example - say 0 has an incoming edge from 1 and 1 has one other
        // outgoing edge to 2. i.e. graph is like 0 <-- 1 --> 2.
        // Although, you don't need to reverse 0 <-- 1 edge, you still have to 
        // make sure that all other edges are coming towards 1. When you call
        // dfs with node 1, you will then recognize the incorrect orientation
        // of 1 --> 2 edge. This is why traversing incoming edges is important.
        
        // Why do we need to erase edges?
        // Ans.
        // To avoid double counting. 
        // We increment the count everytime we see an outgoing edge. We don't 
        // increment for incoming. However, an incoming edge for one node is 
        // the outgoing edge for the other.
        // In the previous example, 0 <-- 1 --> 2.
        // For node 0, we won't increment the count because there are no outgoing
        // edges. But when we are at 1, there are two outgoing edges. But 1 --> 0 
        // is already oriented towards 0 and we don't want to reverse that. How 
        // will we distiguish between correctly oriented edges vs incorrectly 
        // oriented ones in general? Easier approach is to remove those correctly 
        // oriented edges immediately when we know their orientation is correct.
        
        for (int x: out[node]) {
            // There is an edge (node->x). We must reverse it.
            ans++; 
			// delete, edge (x <- node)
            in[x].erase(node);
			// recurse.
            dfs(x);
        }
        for (int x:in[node]) {
		    // The edge is (x <- node). So delete (node -> x).
			out[x].erase(node);
			// recurse.
            dfs(x);
        }
    }
    
    int minReorder(int n, vector<vector<int>>& connections) {
        ans = 0;
		// make graph.
        for (auto x: connections) {
            out[x[0]].insert(x[1]);
            in[x[1]].insert(x[0]);
        }
		// start with node 0.
        dfs(0);
        return ans;
    }
};
