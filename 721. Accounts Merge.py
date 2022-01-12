Actually, what we need to find is this problem are connected components of graph. So, let us do it in two steps:

Construct our graph, iterating over accounts: for each name: look at emails E1, ..., Ek, 
then it is enough to connect E1 with each of the others.
Perform dfs to find connected components, which we keep as comps with correspondences between 
number of component and list of emails in this component. We also keep set seen of visited 
nodes. In the end we just return sort all components and return then.
Complexity
Time complexity is O(a1 log a1 + ... ak * log ak) where ai is the length of accounts[i]. 
Space complexity is O(a1 + ... + ak).

Code
class Solution:
    def accountsMerge(self, accounts):
        names = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                names[email] = name
                
        comps, seen, ans, i = defaultdict(list), set(), [], 0
        def dfs(node, i):
            comps[i].append(node)
            seen.add(node)
            for neib in graph[node]:
                if neib not in seen: dfs(neib, i)
        
        for email in graph:
            if email not in seen:
                dfs(email, i)
                i += 1
        
        return [[names[val[0]]] + sorted(val) for _,val in comps.items()]
Remark
There is also union find solution, but because we need to sort our emails, time complexity, 
even for union find with ranks will be the same as for simple dfs.
