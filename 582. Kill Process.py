

Description,
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:

Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.


HashMap + DFS in Python
we can use a hashmap which stores a particular process value and the list of its direct children.
And then treat it as a tree traversal problem.

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        @solution: hashmap + dfs
        @runtime:  400ms
        @timecomplexity: O(n)
        """
        ret = []
        hm = dict()
        for i in xrange(len(ppid)):
            group = hm.setdefault(ppid[i], [])
            group.append(pid[i])
        self.dfs(hm, kill, ret)
        return ret
    
    def dfs(self, hm, node, ret):
        ret.append(node)
        if node in hm:
            for child in hm.get(node):
                self.dfs(hm, child, ret)
