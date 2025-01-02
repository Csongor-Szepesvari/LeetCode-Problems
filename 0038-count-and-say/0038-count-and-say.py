class Solution:
    def countAndSay(self, n: int) -> str:
        # is the run length encoding of n - 1

        # so "4" -> countAndSay of the result of (3)

        # now we want to return the n-th element
        if n == 1:
            return "1"

        
        unencoded = self.countAndSay(n-1)
        encoded = self.encode(unencoded)
        return encoded
    
    
    def encode(self, unencoded: str) -> str:
        counter = 0
        output = ""
        last_char = ""
        for char in unencoded:
            if char != last_char and last_char!="":
                output += str(counter)+last_char
                counter = 1
            else:
                counter += 1
            last_char = char
        output += str(counter)+last_char

        return output