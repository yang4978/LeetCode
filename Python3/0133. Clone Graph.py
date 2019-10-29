"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        def dfs(node):
            if not node:
                return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val,[])
            lookup[node] = clone
        
            for i in node.neighbors:
                clone.neighbors.append(dfs(i))
            return clone
        return dfs(node)
#         connect = {}
#         node_list = {}
#         deque = [node]
#         used = []
#         while(deque!=[]):
#             temp = deque.pop()
#             used.append(temp)
#             node_list[temp.val] = Node(temp.val,[])
            
#             temp_neighbors = temp.neighbors
            
#             connect[temp.val] = []
            
#             for i in temp_neighbors:
#                 connect[temp.val].append(i.val)
#                 if(i not in used):
#                     deque.append(i)
            
#         for i,neigh in connect.items():
#             temp = []
#             for k in neigh:
#                 temp.append(node_list[k])
#             node_list[i].neighbors = temp

        
#         return node_list[node.val]
