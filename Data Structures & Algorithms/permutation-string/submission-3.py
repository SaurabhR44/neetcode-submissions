class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        for i in range(len(s2)):
            for j in range(i,len(s2)):
                substr = s2[i:j+1]
                sorted_sub = sorted(substr)
                if sorted_sub==sorted(s1):
                    return True
        return False

            