

class Solution {
public:
    vector<int> result; int f=0;
    
    void iscycle(vector<int> graph[], vector<int> &visited, int node){
        
        if(!visited[node]){
            visited[node]=1;
            //result.push_back(node); //we will push the visited nodes to the resulting array

            for(auto edge : graph[node]){
                iscycle(graph,visited,edge);
            
            }
        result.push_back(node);
        visited[node]=2; // if function comes till here then we can mark the current node as 2 i.e, visited
        
        }
        else if(visited[node]==1) f=1;  
    }
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {    
        // create the graph
        vector<int> graph[numCourses];
        
        for(auto edge : prerequisites){
            graph[edge[0]].push_back(edge[1]);
        }
   
        // visited
        //vector<int> visited(numCourses,0);
        vector<int> visited;
        visited.resize(numCourses);
        for (int i=0;i<numCourses;++i){
            iscycle(graph, visited, i);
        }
        
        if(f)
            return vector<int>();
        //result.erase(result.begin());
        return result;    
    }
};
