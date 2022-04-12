Question:
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one 
flight. Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from "JFK", thus, the 
itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest 
lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
   
    MUC--->LHR--->SFO
     |>            |
     |             |>
    JFK           SJC
    
Solution: Euler path

Actually, in this problem we are asked to find Euler path, smallest lexically. There is classical algorithm with complexity O(E). Starting from 
the starting vertex v, we build a path by adding at each step an edge that has not yet been passed and is adjacent to the current vertex. The 
vertices of the path are accumulated in stack S. When the moment comes when for the current node w all the incident edges have already passed, 
we write the vertices from S in output until we meet the node where the incident has not passed yet edges. Then we continue our traversal of 
the unattended edges. It can be written both with recursion or with stack, recursion version is shorter.

Here is a link, where you can plunge deeper into this:
http://www.graph-magics.com/articles/euler.php

If you neves saw this problem and even if you know what Euler path is, I think it is almost impossible to invent this algorighm by yourself, 
and this problem should be marked as hard.

Complexity: time and space complexity of usual Euler Path Finding algorighm is O(E+V) = O(E), because we traverse each edge only once and number 
of edges is more than number of vertixes - 1 in Eulerian graph. However as @ainkartik203 mentioned, here we sort our list for every node, so 
complexity will be O(ElogE).

class Solution:
    def dfs(self, airport):
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)
            
    def findItinerary(self, tickets):
        self.route = []
        self.adj_list = defaultdict(list)
        for i,j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list: 
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)
            
        self.dfs("JFK")
        return self.route[::-1]
