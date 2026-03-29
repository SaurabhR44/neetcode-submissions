class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            first,second = self.firstnsecond(stones)
            if first==second:
                stones.remove(first)
                stones.remove(second)
            if first!=second:
                stones.append(first-second)
                stones.remove(first)
                stones.remove(second)
        return stones[0] if stones else 0



    def firstnsecond(self,stones:List[int]) -> tuple[int,int]:
        sorted_stones = sorted(stones)
        n = len(sorted_stones)
        return [sorted_stones[n-1],sorted_stones[n-2]]
