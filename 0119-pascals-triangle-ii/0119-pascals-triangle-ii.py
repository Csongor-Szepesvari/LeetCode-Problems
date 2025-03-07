class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # this is just binomial theorem
        
        from math import comb

        output = []
        for k in range(rowIndex+1):
            output.append(comb(rowIndex, k))


        return output