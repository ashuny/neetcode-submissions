class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            countS, countT = {}, {}
            for ss in s:
                countS[ss] = 1 + countS.get(ss, 0)
            for tt in t:
                countT[tt] = 1 + countT.get(tt, 0)
            if countS == countT:
                return True
            else:
                return False
                    



        