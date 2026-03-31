class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task,0)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)
        time = 0
        q = deque()  # [cnt,idleTime]

        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap)-1
                if cnt:
                    q.append([cnt,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap,q.popleft()[0])
        return time
                
