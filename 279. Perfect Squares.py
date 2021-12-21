Solution — Dynamic Programming
This problem is a classic dynamic programming problem that we can use previous information to construct current value by following formula:
For any integer 0 < k ≤ n, D[k] = min(1 + D[k-l²]),
where l is an integer and 0 < l < SQRT(k)
Then our answer will be at D[n].



https://lenchen.medium.com/leetcode-279-perfect-squares-d83cac919604

# Python3

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # approach: use dynamic programming for finding minimum 
        #           distance by previous information:
        #           for each k <= n,
        #               d[k] = min(1 + d[k-(l**2)]),
        #               where 0 < l < sqrt(k) and l is an integer

        # d[0] = 0 because n is a positive integer
        distance = [0 for i in range(n+1)]

        for i in range(1, n+1):
            count = square = 1
            min_distance = n
            while square <= i:
                check_distance = 1 + distance[i-square]
                if check_distance < min_distance:
                    min_distance = check_distance
                count += 1
                square = count * count
            distance[i] = min_distance

        return distance[n]
