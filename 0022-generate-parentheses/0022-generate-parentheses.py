class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n PAIRS of parentheses, generate a list of all well-formed parentheses
        self.parentheses = []
        self.recursive("", 0, n)

        return self.parentheses

    def recursive(self, string_down, open_p, n):
        #print(self.parentheses)
        if n == 0:
            self.parentheses.append(string_down+(")"*open_p))
            return
        
        if open_p==0:
            self.recursive(string_down+"(", open_p+1, n-1)
        else:
            self.recursive(string_down+"(", open_p+1, n-1)
            self.recursive(string_down+")", open_p-1, n)