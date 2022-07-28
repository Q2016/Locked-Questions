Question:
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account. Now, we would like to merge these accounts. Two accounts 
definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, 
they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their 
accounts definitely have the same name. After merging the accounts, return the accounts in the following format: the first element of each 
account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.    





Solution: DFS and union find
    https://www.youtube.com/watch?v=E8EKDyGtRN0
Actually, what we need to find in this problem are connected components of graph. So, let us do it in two steps: Construct our graph, 
iterating over accounts: for each name: look at emails E1, ..., Ek, then it is enough to connect E1 with each of the others.
Perform dfs to find connected components, which we keep as comps with correspondences between number of component and list of emails in this 
component. We also keep set seen of visited nodes. In the end we just return sort all components and return then.


    def accountsMerge(self, accounts):

        def dfs(node, i):
            comps[i].append(node)
            seen.add(node)
            for neib in graph[node]:
                if neib not in seen: dfs(neib, i)
                    
        names = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                names[email] = name       
                
        comps, seen, ans, i = defaultdict(list), set(), [], 0
      
        for email in graph:
            if email not in seen:
                dfs(email, i)
                i += 1     
        return [[names[val[0]]] + sorted(val) for _,val in comps.items()]

    

Complexity
Time complexity is O(a1 log a1 + ... ak * log ak) where ai is the length of accounts[i]. 
Space complexity is O(a1 + ... + ak).
