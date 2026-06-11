class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #logic : the length of the 2 strings must be same 
        return sorted(s)==sorted(t)
        