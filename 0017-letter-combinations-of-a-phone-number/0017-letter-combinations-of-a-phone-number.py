class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # to generate all mappings, at every step we will iterate through the existing answer
        # and generate new mappings, storing them in a new list then overwriting our original ans
        ans = [""]

        for digit in digits:
            temp = []
            possible_outcomes = mappings[digit]
            for item in ans:
                for mapping in possible_outcomes:
                    temp.append(item+mapping)

            ans = temp
        
        return ans


        
