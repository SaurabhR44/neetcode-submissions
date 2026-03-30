class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = x*x + y*y
            heap.append((dist,[x,y]))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result