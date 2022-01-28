Question:
Given an integer n, return the least number of perfect square numbers that sum to n. A perfect square is an integer that 
is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 
are perfect squares while 3 and 11 are not.    


Solution : Dynamic Programming
This problem is a classic dynamic programming problem that we can use previous information to construct current value by following formula:
For any integer 0 < k ≤ n, D[k] = min(1 + D[k-l²]),
where l is an integer and 0 < l < SQRT(k)
Then our answer will be at D[n].


    def numSquares(self, n):

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
