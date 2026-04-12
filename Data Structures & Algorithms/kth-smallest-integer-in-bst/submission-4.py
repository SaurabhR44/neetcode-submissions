import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Python's heapq is a min-heap, so we store negative values 
        # to simulate a max-heap behavior.
        max_heap = []
        
        def dfs(node):
            if not node:
                return
            
            # Push negative value into heap
            heapq.heappush(max_heap, -node.val)
            
            # If heap grows larger than k, remove the largest (top)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        # The root of our max-heap is the kth smallest value
        # Multiply by -1 to revert to the original number
        return -max_heap[0]