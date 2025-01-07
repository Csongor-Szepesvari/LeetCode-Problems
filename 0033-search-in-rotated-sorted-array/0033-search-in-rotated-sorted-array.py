class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rotation means that at some index k
        # it gets chopped ie k -> 1, 1 -> n + 1, k - 1 -> n + k - 1

        # given the array nums post-roation and an integer target
        # return the index of target if it is in nums or -1 if its not in nums

        # must run in log n, can't search for where the rotation is

        # run a normal binary search until we hit a rotation
        n = len(nums)
        l = 0
        r = n-1
        
        
        # if its rotated its guaranteed that the stuff past the point of rotation is smaller


        while l <= r:
            m = (l+r)//2
            checking = nums[m]
            print(l,r,m,checking, target)
            if checking == target:
                return m
            
            if nums[l] <= checking:
                # we know the left part of the array is standard

                if target >= nums[l]:
                    # if it's greater than the smallest in the left
                    if target == nums[l]:
                        # if its exactly the smallest in the left
                        return l
                    if target < checking:
                        # if its less than middle
                        r = m - 1
                        continue
                    else:
                        # if its greater than middle
                        l = m + 1
                        continue
            else:
                # we know the left part of the array is not correctly sorted
                # suppose we have [0,1,2,3,4,5,6,7]
                # twisted to [5,6,7,0,1,2,3,4]
                # if its greater than array[0] it will be guaranteed to be here
                # if its less than array[m] it will be here
                if target >= nums[l]:
                    if nums[l] == target:
                        return l
                    else:
                        r = m - 1
                        continue
                elif target < checking:
                    r = m - 1
                    continue
                else:
                    l = m + 1
                    continue

            if nums[r] >= checking:
                # we know the right of the array is standard
                if target <= nums[r]:
                    # if it's leq than the largest in the right
                    if target == nums[r]:
                        # if its exactly the largest in the right
                        return r
                    if target > checking:
                        # if its more than middle
                        # we know that its in the right section
                        l = m + 1
                    else:
                        # if its less than middle
                        r = m - 1
            else:
                # we know the right part of the array is not correctly sorted
                # suppose we have [0,1,2,3,4,5,6,7]
                # twisted to [3,4,5,6,7,0,1,2]
                # if its less than array[r] it will be guaranteed to be here
                # if its greater than array[m] it will be here
                if target <= nums[r]:
                    if nums[r] == target:
                        return r
                    else:
                        l = m + 1
                elif target > checking:
                    l = m + 1
                else:
                    r = m - 1
    
        return -1
