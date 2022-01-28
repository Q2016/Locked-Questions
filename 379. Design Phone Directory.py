Question
Design a Phone Directory which supports the following operations:
get: Provide a number which is not assigned to anyone. check: Check if a number is available or not. release: Recycle or release a number.

    
Solution:
    def __init__(self, maxNumbers):
        self.__curr = 0
        self.__numbers = range(maxNumbers)
        self.__used = [False] * maxNumbers
 
    def get(self):
        if self.__curr == len(self.__numbers):
            return -1
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = True
        return number
 
    def check(self, number):
        return 0 <= number < len(self.__numbers) and not self.__used[number]
 
    def release(self, number):
        if not 0 <= number < len(self.__numbers) or not self.__used[number]:
            return
        self.__used[number] = False
        self.__curr -= 1
        self.__numbers[self.__curr] = number
 
　
# init:     Time: O(n), Space: O(n)
# get:      Time: O(1), Space: O(1)
# check:    Time: O(1), Space: O(1)
# release:  Time: O(1), Space: O(1)
