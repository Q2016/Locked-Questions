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
    
Solution: Backtracking+ DFS

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        
        if len(tickets) == 0:
            return []
        
        tickets = sorted(tickets, key=lambda x:(x[0], x[1]))
        self.visited = defaultdict(list)
        self.adjacency_li = defaultdict(list)
        
        def createGraph(s, d):
            self.adjacency_li[s].append(d)
            self.visited[s].append(False)
            return

        for ticket in tickets:
            s = ticket[0]
            d = ticket[1]
            createGraph(s, d)

        def DFS(so):
            
            if len(self.output) ==len(tickets)+1:
                return True
            for i, dest in enumerate(self.adjacency_li[so]):
                #print(self.output)
                if self.visited[so][i]==False:
                    self.output.append(dest)
                    self.visited[so][i] = True
                    ret = DFS(dest)
                    if ret == True:
                        return True
                    self.output.pop()
                    self.visited[so][i] = False
            return False
