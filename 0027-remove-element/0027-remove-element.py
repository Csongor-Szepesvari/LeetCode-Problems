class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # simply loop through the list and make swaps to the back
        # control the special cases, when its length 0 or 1
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            if nums[0] != val:
                return 1
            else:
                return 0

        # make two pointers last and first
        l_index = len(nums)-1
        f_index = 0

        # loop until they are stacked on top of each other
        while f_index < l_index:
            print(f_index, l_index)
            if nums[f_index] == val:
                print("found number to swap at", f_index)
                while nums[l_index] == val and f_index < l_index:
                    l_index -= 1
                if f_index == l_index:
                    return f_index
                else:
                    nums[f_index], nums[l_index] = nums[l_index], nums[f_index]    
            f_index += 1
        if nums[f_index] != val:
            f_index += 1
        return f_index

        # in the case of 4,5
        # i = 0, last_pointer = 1
