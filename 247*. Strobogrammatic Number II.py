Question:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example: 
Given n = 2, return ["11","69","88","96"].













Solution:

A strobogrammatic number is a number that looks the same when rotated 180 degrees. So which are the strobogrammatic number? 
0, 1, 8 are the digits that are strobogrammatic. 6 and 9, when used together, form strobogrammatic numbers.    

One way to solve this problem is by creating a dictionary that stores each number that can form a strobogrammatic number and its corresponding values.

char_list = ["0", "1", "6", "8", "9"]
strobogrammatic_dict = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
We will use 2 strings; one to save the number formed another to save its possible rotated number. When the number of digits is equal to n, 
if the number formed is equal to the number saved in a rotated number, we will save it as part of the result.

class StrobogrammaticFinder:
  def findStrobogrammatic(self, n: int) -> List[str]:
      output = []
      char_list = ["0", "1", "6", "8", "9"]
      strobo_dict = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
      def dfs(tmp, st_tmp):
          if len(tmp) == n:
             if tmp == st_tmp[::-1]:
                if str(int(tmp)) == tmp:
                   output.append(tmp)
             return
          for i in range(len(char_list)):
              dfs(tmp+char_list[i],st_tmp+strobo_dict[char_list[i]])
           
      dfs("","")
      return(output)
    
Complexity analysis.

Time Complexity
For all n digits, we have 5 digits to choose from. Hence time complexity is O(5^N).

Space Complexity
Since we are recursively calling the dfs function, and internally recursive calls are stored in form of a stack. The space complexity is O(5^N).
    
    
Do we have to find numbers for all the n places? Can we try to find only until the half portion? If we find just until the half position, 
we can rotate this number and set it for the other half. Or even better, we start from both the extreme positions and move inwards.

Let us see how we can code this.

class StrobogrammaticFinder:
  def findStrobogrammatic(self, n: int) -> List[str]:
        output = []
        # Create a dictionary
        strobo_dict = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        start = 0
        end = n-1
        #Create a list of size n initialised with None
        result = [None]*n
        self.dfs(start, end, result, strobo_dict, output)
        return output
    
  def dfs(self, start, end, result, strobo_dict, output):
        if start > end:
            output.append(''.join(result))
            return
        #For each number in the dictionary
        for each_num in strobo_dict:
            #if it is single digit number
            if start!= end and each_num == '0' and start == 0:
                continue
            # if we have reached the middle
            if start == end and each_num in ('6','9'):
                continue
                
            result[start], result[end] = each_num, strobo_dict[each_num]
            self.dfs(start+1, end-1, result, strobo_dict, output)

Complexity analysis
Time Complexity
For all n digits, we have 5 digits to chose from, but in the above code, we start from both the extreme positions and move inwards. 
Hence time complexity is O(5^(N/2)).

Space Complexity
Since we are recursively calling the dfs function, and internally recursive calls are stored in form of a stack. The space complexity is O(5^(N/2)).



Another version but not very clear:
    
Recursion: T(n) = append each string with ("1", "1"); ("6","9"); ("9","6"); ("8","8"); 
if not at the out-most recursion; also add ("0","0") from returned element from T(n - 2); 
Base case: (n =0 => ['']; n = 1=>['0', '1', '8'])
Without Recursion: reverse the order with for loop

    def findStrobogrammatic(self, n):

        def helper(cur_len, total_len):
            # base case 
            if cur_len == 0: return ['']
            if cur_len == 1: return ['0', '1', '8']
            ans = []
            sub = helper(cur_len - 2, total_len)

            for s in sub:
                if cur_len != total_len:
                    ans.append("0" + s + "0")
                ans.append("1" + s + "1")
                ans.append("6" + s + "9")
                ans.append("8" + s + "8")
                ans.append("9" + s + "6")
            return ans

        return helper(n, n)
                
                
# Time:  O(n^2 * 5^(n/2)) # not sure if n^2 is correct
# Space: O(n)                # space seems right




