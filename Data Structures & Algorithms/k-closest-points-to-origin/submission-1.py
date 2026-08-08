import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2
        
        heap = []
        for x,y in points:
            d = dist(x,y)
            heapq.heappush(heap, (-d, x, y))
        
        for _ in range(len(points) - k):
            heapq.heappop(heap)
        
        return [(x,y) for (d, x, y) in heap ]
            