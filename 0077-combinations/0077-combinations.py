class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # given two integers n and k, return all possible combinations of k numbers
        # chosen from the range 1 through n
        #print(list(range(1,n+1)))

        #print("Generating options for", n, "choose", k)

        if k == 0:
            return [[]]
        if n == k:
            return [list(range(1,n+1))]

        # we will do this recursively, create one where we select this one and pass it along

        # select the first
        comb1 = self.combine(n-1, k-1)
        
        if len(comb1) == 0:
            comb1.append([n])
        else:
            for sub_list in comb1:
                sub_list.append(n)
        #print("When selecting current", n, "choose", k, "combinations are", comb1)
        #print()

        
        # don't select the first
        comb2 = self.combine(n-1, k)
        #print("When not selecting current for", n, "choose", k, "combs are", comb2)
        
        
        comb1.extend(comb2)

        return comb1
        