Question:
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
This is just like a tree structure. Only 0 has no parent process.  
Now given a process you want to kill, return a list of PIDs of processes that will be killed in the end. 
when a process is killed, all its children processes will be killed. 

Example 1:
Input: 
pid =  [1, 3, 10, 5], ppid = [3, 0, 5, 3], kill = 5, Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.









Solution: BFS 
 https://www.youtube.com/watch?v=pXXJMCtGbiI
           
class Solution:
    def killProcess(self, pid, ppid):
        node_dic=defaultdict(list)
        
        for i, pp in enumerate(ppid):
           node_dic[pp].append(pid[i])
           
        queue=collections.deque([kill])
        result=[]
        while queue:
           parent_node=queue.popleft()
           result.append(parent_node)
           
           queue.extend(node_dic[parent_node])
        
        return result


           
