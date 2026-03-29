class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        min_rate = r
        while l<=r:
            k = l + ((r-l)//2)
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            
            if time<=h:
                min_rate = min(min_rate,k)
                r = k-1
            else:
                l = k+1
        return min_rate