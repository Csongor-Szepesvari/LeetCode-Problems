class Solution:
    def canWinNim(self, n: int, memo_winning=None) -> bool:
        # 1 2 3 are winning
        # so 4 is not
        # 5 can force 4 so winning
        # same w 6 and 7
        # but 8 is not
        return n % 4 != 0
        