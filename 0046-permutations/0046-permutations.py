class Solution:

    # Given an array nums of distinct integers, return all the possible permutations.
    # You can return the answer in any order.
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # nums contains the digits to permute
        all_answers = []
        n = len(nums)
        if n == 1:
            return [nums]

        for i in range(n):
            new_list = []
            if i > 0:
                new_list += nums[0:i]
            if i < n-1:
                new_list += nums[i+1:]
            sub_class = self.permute(new_list)
            #print(new_list)
            #print(sub_class)
            #print([nums[i]])
            #print()
            all_answers += [[nums[i]] + element for element in sub_class]

        return all_answers