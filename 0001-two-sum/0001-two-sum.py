class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aDict = {}
        # Chunk 1: aDict is a dictionary using key value pairs where the key is the values of the nums list
        # the values are the indeces
        for i in range(len(nums)):
            if nums[i] in aDict:
                aDict[nums[i]] = [aDict[nums[i]], i]
            else:
                aDict[nums[i]] = i
        

        # Loop through each element of the list
        # 
        for i in range(len(nums)):
            y = target - nums[i]
            if y in aDict:
                maybe_list = aDict[y]
                if type(maybe_list) == list:
                    if i == maybe_list[0]:
                        return [i, maybe_list[1]]
                    else:
                        return [i, maybe_list[0]]
                elif maybe_list != i:
                    return [i, maybe_list]