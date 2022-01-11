//Any time we try to initiate depth first search on a node that is already colored //"gray" 
(is being processed) that means we have encountered a cycle in this //directed graph and can 
return False. This model can also be used for topological //sorting

//White (unvisited) -> Gray (visiting) -> Black (visited)
//https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/

class Solution {
public:
    bool iscycle(vector<int> graph[],vector<int> &visited,int i){
        if(visited[i]==1)
            return true;
        
        if(visited[i]==0){
            visited[i]=1;
            for(auto edge : graph[i]){
                if(iscycle(graph,visited,edge))
                    return true;
            }
        }
        
        visited[i] = 2;
        return false;
    }
    
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        
        vector<int> graph[numCourses];
        
        for(auto edge : prerequisites)
            graph[edge[1]].push_back(edge[0]);
        
        vector<int> visited(numCourses,0);
        
        for(int i=0;i<numCourses;i++){
            if(iscycle(graph,visited,i))
                return false;
        }
        return true;
    }
};
