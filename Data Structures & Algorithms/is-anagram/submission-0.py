class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        elif len(s) == 0 and len(t) >0:
            return False
        elif len(s) != len(t):
            return False
        else:
            for ss in s:
                if ss not in t:
                    return False
                else:
                    t = t.replace(ss, "", 1)
                    s = s.replace(ss, "", 1)
            return True
                    



        