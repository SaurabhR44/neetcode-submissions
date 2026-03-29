class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        l=0
        res = 0

        for r in range(len(s)):
            if s[r] in last_index:
                l = max(last_index[s[r]]+1,l)
            last_index[s[r]] = r
            res = max(res,r-l+1)
        return res

