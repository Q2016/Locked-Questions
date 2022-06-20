Question:
On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.
You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least 
one ship in the rectangle represented by the two points, including on the boundary.
Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is 
guaranteed that there are at most 10 ships in that rectangle.
Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will 
result in disqualification.

Example :
Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.  
  
  
  
  
  
  
  
  
Solution:  Recursion (divided and conquer)

  
class Solution(object):
  def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
    if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
      return 0
    if not sea.hasShips(topRight, bottomLeft):
      return 0

    # sea.hashShips(topRight, bottomLeft) == True
    if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
      return 1

    mx = (topRight.x + bottomLeft.x) // 2
    my = (topRight.y + bottomLeft.y) // 2
    ans = 0
    # top right
    ans += self.countShips(sea, topRight, Point(mx + 1, my + 1))
    # bottom right
    ans += self.countShips(sea, Point(topRight.x, my),
                           Point(mx + 1, bottomLeft.y))
    # top left
    ans += self.countShips(sea, Point(mx, topRight.y),
                           Point(bottomLeft.x, my + 1))
    # bottom left
    ans += self.countShips(sea, Point(mx, my), bottomLeft)
    return ans
      
      
Time: O(logMN)
Space: O(logMN)      
