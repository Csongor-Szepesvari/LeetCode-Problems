class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Given two non-negative integers num1 and nume2 represented as strings
        # return the product of num1 and num2, also represented as a string

        # you must not use any built-in BigInteger library or convert the inputs to integers directly.

        
        # plan -> reverse the strings, iterate through them, multiply them across

        num1 = num1[::-1]
        num2 = num2[::-1]
        total = 0

        for i in range(len(num1)):
            digit_num1 = int(num1[i])*(10**i)
            for j in range(len(num2)):
                digit_num2 = int(num2[j])*(10**j)
                total += digit_num1*digit_num2

        return str(total)