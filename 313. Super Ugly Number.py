Question:
A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].  
  







  
  
Solution:
The idea is from Ugly Number II:
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer n, return the nth ugly number.	

public int nthUglyNumber(int n){
	int i2=0, i3=0, i5=0;
	int[] k = new int[n];
	k[0] = 1;
	for (int i=1; i<n; i++) {
		k[i] = Math.min(k[i2]*2, Math.min(k[i3]*3, k[i5]*5));
		if (k[i]%2 == 0) i2++;
		if (k[i]%3 == 0) i3++;
		if (k[i]%5 == 0) i5++;
	}
	return k[n-1];
}

Similarly, for this problem, just use loop to replace above i2, i3, i5.

public int nthSuperUglyNumber(int n, int[] primes) {
    int len = primes.length;
    int[] index = new int[len]; //index[0]==0, ... index[len-1]==0
    int[] res = new int[n];
    res[0] = 1;
    for(int i=1; i<n; i++) {
        int min = Integer.MAX_VALUE;
        for(int j=0; j<len; j++){
            min = Math.min(res[index[j]]*primes[j], min);
        }
        res[i] = min;
        for (int j=0; j<len; j++) {
            if(res[i]%primes[j]==0) index[j]++;
        }
    }
    return res[n-1];
}

Complexity: O(n*k): nth number, k number of primes
