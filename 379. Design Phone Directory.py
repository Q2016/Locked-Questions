Question
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.

Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2)



# init:     Time: O(n), Space: O(n)
# get:      Time: O(1), Space: O(1)
# check:    Time: O(1), Space: O(1)
# release:  Time: O(1), Space: O(1)
class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.__curr = 0
        self.__numbers = range(maxNumbers)
        self.__used = [False] * maxNumbers
 
    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.__curr == len(self.__numbers):
            return -1
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = True
        return number
 
 
    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return 0 <= number < len(self.__numbers) and \
               not self.__used[number]
 
    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not 0 <= number < len(self.__numbers) or \
           not self.__used[number]:
            return
        self.__used[number] = False
        self.__curr -= 1
        self.__numbers[self.__curr] = number
 
# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)　　
