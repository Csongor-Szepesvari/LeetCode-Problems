class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        explored = set([])
        num_islands = 0

        def neighbours_to_add(r,c):
            to_check = []
            if r-1 >= 0:
                if not (r-1,c) in explored:
                    to_check.append((r-1,c))
            if r+1 < m:
                if not (r+1,c) in explored:
                    to_check.append((r+1,c))
            if c-1 >= 0:
                if not (r,c-1) in explored:
                    to_check.append((r, c-1))
            if c+1 < n:
                if not (r,c+1) in explored:
                    to_check.append((r, c+1))
            
            return to_check

        from collections import deque
        q = deque([]) 
        
        for y in range(m):
            for x in range(n):
                if not (y,x) in explored:
                    test = (y,x)
                    if grid[y][x] == "1":
                        num_islands += 1
                        q.append(test)
                        while q:
                            item = q.popleft()
                            r = item[0]
                            c = item[1]
                            explored.add((r,c))
                            if grid[r][c] == "1":
                                list_items = neighbours_to_add(r,c)
                                for _item in list_items:
                                    q.appendleft(_item)

        return num_islands
                            
                            

            
            
            


        # for every object, we check its neighbours (that haven't been visited yet)
        