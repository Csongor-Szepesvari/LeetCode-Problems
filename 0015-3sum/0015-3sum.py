class Solution:
    def __init__(self):
        self.myDict = {}
        self.contained = set()
        self.checked = set()

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # load up our dictionary with our terms
        for i in range(n):
            val = nums[i]
            if val in self.myDict:
                self.myDict[val].append(i)
            else:
                self.myDict[val] = [i]
        #print(self.myDict)

        loc_contained = set()
        valid = []

        for i in range(n):
            val = nums[i]
            if not val in self.checked:

                target = -val
                items = self.twoSum(nums, target, i)
                #print(items)
                # translate the indices into values
                for item in items:
                    
                    loc_val = sorted([nums[item[0]], nums[item[1]], nums[item[2]]])
                    #print(loc_val)
                    tv = tuple(loc_val)
                    if not tv in loc_contained:
                        #print("supposed to append")
                        valid.append(loc_val)
                        loc_contained.add(tv)
                self.checked.add(val)
            
            #print(valid)
        
        return valid


    def twoSum(self, nums: List[int], target: int, exclude: int) -> List[List[int]]:
        # step through the list, adding elements to a dictionary as we go

        # we need to find all solutions, not just 1 solution for a given target
        # use the same global dictionary, but exclude any solutions with "exclude" as an index
        toRet = []
        for i in range(len(nums)):
            if i != exclude:
                look_for = target-nums[i]
                if look_for in self.myDict:
                    # grab all answers that equal this, loop through them
                    # remove the ones that contain exclude or i
                    allAnswers = self.myDict[look_for]
                    found = False
                    index = 0
                    while not found and index < len(allAnswers):
                        lf = allAnswers[index]
                        if exclude == lf or i == lf:
                            pass
                        else:
                            val = sorted([lf,i,exclude])
                            tup_val = tuple(val)
                            found = True
                            if not tup_val in self.contained:
                                toRet.append(val)
                                self.contained.add(tup_val)
                        index += 1
                
        return toRet
