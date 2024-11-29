class Solution:
    def reverse(self, x: int) -> int:

        # 32 bit signed integer range is 
        # [(-2^31), (2^31)-1]
        max_val = 2**31-1
        min_val = -1 * 2**31

        if x < 0:
            neg = True
        else:
            neg = False
        x = str(abs(x))
        
        multiplier = 1
        val = 0
        # if the value is negative, we add local value to the negative max
        #   if the value is positive we subtract the local value to the positive max
        #

        for digit in x:
            local_val = int(digit) * multiplier
            if neg:
                min_val += local_val
                if min_val > 0:
                    return 0
            else:
                max_val -= local_val
                if max_val < 0:
                    return 0
            val += local_val
            multiplier *= 10


        if neg:
            return -1*val
        return val
        


        return val
        