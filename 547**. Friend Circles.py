Question:
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:     Output: 2
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.




No link, this is repeatative number of provinces

Solution: DFS
We are using the dfs to find the students’ friends and the student’s friends’ friends 
and so on and store them as 1 friend circle. If other student in this circle then we skip 
until we find a student not in this circle, this student will start another circle.


     def findCircleNum(self, M: List[List[int]]) -> int:
             visited = set()
             count = 0
             def dfs(student, visited):
                 for class_mate, is_friend in enumerate(M[student]):
                     if class_mate not in visited and is_friend:
                         visited.add(class_mate)
                         dfs(class_mate, visited)

             for student in range(len(M)):
                 if student not in visited:
                     visited.add(student)
                     count+=1
                     dfs(student, visited)
             return count

Time complexity is O(n^2)
