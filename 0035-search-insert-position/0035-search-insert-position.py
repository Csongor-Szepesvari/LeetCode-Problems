class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # searchInsert, just look where you would normally insert into
        # performm a binary search, if there return that index

        # else return the index it splits
        r = len(nums)-1
        l = 0
        m = (r-l)//2


        while nums[m] != target:
            print(l,r,m)
            if l == r:
                if nums[l] < target:
                    return l+1
                return l
            
            if target > nums[m]:
                if target <= nums[m+1]:
                    return m+1
                else:
                    l = m+1

            elif target < nums[m]:
                if target >= nums[m-1]:
                    if target == nums[m-1]:
                        return m-1
                    return m
                else:
                    r = m

            m = l+(r-l)//2
        
        return m

