# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #given the root of a binary tree, return the:
        #   zigzag level order traversal of its nodes' values
        # that is from left to right, then right to left the next level and alternate between

        # do a BFS, level based descent with a queue
        from collections import deque

        q = deque()

        node = root

        output = []
        q.append((0,node))
        level_output = []

        last_depth = -1
        while q:
            #print(q)
            #print(len(q))
            #print()
            q_node = q.popleft()
            depth = q_node[0]
            # ensure node isn't none
            if q_node[1]:
                val = q_node[1].val
                # new depth reached
                if last_depth != depth:
                    # if its not the first level
                    if level_output != []:
                        # if its an odd level we reverse it
                        if last_depth%2==1:
                            level_output.reverse()
                        # add it to the output
                        output.append(level_output)
                    # restart the level_output
                    level_output = [val]
                else:
                    level_output.append(val)

                # in either case, we need to update last depth and add left and right
                last_depth = depth
                q.append((depth+1, q_node[1].left))
                q.append((depth+1, q_node[1].right))
        if level_output != []:
            if last_depth%2==1:
                level_output.reverse()
            # add it to the output
            output.append(level_output)

        return output
            
