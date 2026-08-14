class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for s, dst, weight in edges:
            adj[s].append((dst, weight))

        shortest = {}
        minHeap = [(0, src)]
        while minHeap:
            distance, node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = distance

            for node2, distance2 in adj[node]:
                if node2 not in shortest:
                    heapq.heappush(minHeap, (distance2 + distance, node2))
            
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest
