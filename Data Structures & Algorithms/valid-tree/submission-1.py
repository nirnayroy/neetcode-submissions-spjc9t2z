class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        prev = -1
        visited = []
        print(adj)

        def dfs(node, prev, visited):
            
            if node in visited and node != prev:
                return False
            visited.append(node) # [0, 1, 3]
            # 1
            for child in adj[node]:
                if child != prev:
                    
                    if not dfs(child, node, visited):
                        return False
                    
            return True
                

        
        cycle = dfs(0, prev, visited)
        print(cycle)
        return cycle and len(visited) == n

        