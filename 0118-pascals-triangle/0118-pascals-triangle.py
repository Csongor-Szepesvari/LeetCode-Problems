class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:

        output = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                #print(i,j)
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(output[i-1][j-1]+output[i-1][j])
            
            output.append(temp)
            #print(output)

        return output


        