class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums is sorted in non-decreasing order
        # find starting and ending position of a given target value
        # (find the smallest number with this value and find the largest number with this value)

        # -1, -1 if not present

        # use bin search to get to the desired value then scroll both directions
        n = len(nums)

        def bin_search(l, r):
            if l<0 or l>r or r>=n or r < l:
                return -1
            
            to_check = l + (r-l)//2
            if nums[to_check] == target:
                return to_check

            elif nums[to_check] < target:
                l = to_check+1
            
            else:
                r = to_check-1

            return bin_search(l,r)

        #some_index = bin_search(0,n-1)

        def search_neighbourhood(index):
            if index == -1:
                return [-1,-1]

            lower_bound = index
            upper_bound = index
            while lower_bound >= 0 and nums[lower_bound] == target:
                lower_bound -= 1
            while upper_bound < n and nums[upper_bound] == target:
                upper_bound += 1
            
            return [lower_bound+1, upper_bound-1]

        return search_neighbourhood(bin_search(0,n-1))
            