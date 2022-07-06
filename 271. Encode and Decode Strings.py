Question:
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network 
and is decoded back to the original list of strings.

Machine 1 (sender) has the function:                  Machine 2 (receiver) has the function:

def encode(vector strs):                              def decode(string s) {
  // ... your code                                       //... your code
  return encoded_string;                              return strs;

Implement the encode and decode methods.

 
  
  
We can just use the ord and use ASCII codes  
  
Solution:  
  
class Codec:
    def encode(self, strs): 
        return ''.join(s.replace('|', '||') + ' | ' for s in strs) 
    def decode(self, s): 
        return [t.replace('||', '|') for t in s.split(' | ')[:-1]]
