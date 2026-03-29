class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s1)
        for i in range(len(s2)-n+1):
            substr = s2[i:i+n]
            if sorted(substr) == s1:
                return True
        return False