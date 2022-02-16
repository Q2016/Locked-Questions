Question:
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, 
and they should not go into the same group. Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the 
person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].	


Solution: DFS and coloring	
https://leetcode.com/problems/possible-bipartition/discuss/654955/Python-sol-by-DFS-and-coloring.-w-Graph

The question asks us to divide given people into two groups such that no two people in the same group dislike each other.
For ease of understanding, we can represent this problem as a graph, with people being the vertices and dislike-pairs being the edges of this graph.
We have to find out if the vertices can be divided into two sets such that there aren't any edges between vertices of the same set. A graph satisfying 
this condition is called a bipartite graph. 
We try to color the two sets of vertices, with RED and BLUE colors. In a bipartite graph, a RED vertex must be connected only with BLUE vertices 
and a BLUE vertex must be connected only with RED vertices. In other words, there must NOT be any edge connecting two vertices of the same color. 
Such an edge will be a conflict edge.
The presence of conflict edges indicate that bipartition is NOT possible.

The graph may consist of many connected components. For each connected component, we run our BFS algorithm to find conflict edges, if any. For each component, 
we start by coloring one vertex RED, and all it's neighbours BLUE. Then we visit the BLUE vertices and color all their neighbours as RED, and so on. 
During this process, if we come across any RED-RED edge or BLUE-BLUE edge, we have found a conflict edge and we immediately return false, as bipartition 
will not be possible.
If no conflict edges are found at the end of the algorithm, it means bipartition is possible, hence we return true.




class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        # Constant defined for color drawing to person
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
        # -------------------------------------
        
        def helper( person_id, color ):
            
            # Draw person_id as color
            color_table[person_id] = color
            
            # Draw the_other, with opposite color, in dislike table of current person_id
            for the_other in dislike_table[ person_id ]:
   
                if color_table[the_other] == color:
                    # the_other has the same color of current person_id
                    # Reject due to breaking the relationship of dislike
                    return False

                if color_table[the_other] == NOT_COLORED and (not helper( the_other, -color)):
                    # Other people can not be colored with two different colors. 
					# Therefore, it is impossible to keep dis-like relationship with bipartition.
                    return False
                    
            return True
        
        
        # ------------------------------------------------
		
		
        if N == 1 or not dislikes:
            # Quick response for simple cases
            return True
        
        
        # each person maintain a list of dislike
        dislike_table = defaultdict( list )
        
        # key: person ID
        # value: color of person
        color_table = defaultdict(int)
        
        for p1, p2 in dislikes:
            
            # P1 and P2 dislike each other
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        
        # Try to draw dislike pair with different colors in DFS
        for person_id in range(1, N+1):
            
            if color_table[person_id] == NOT_COLORED and (not helper( person_id, BLUE)):
                # Other people can not be colored with two different colors. 
				# Therefore, it is impossible to keep dis-like relationship with bipartition.
                return False 
        
        return True
