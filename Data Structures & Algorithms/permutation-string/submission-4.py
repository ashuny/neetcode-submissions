class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count_1 = {}
        count_2 = {}
        l, r = 0, len(s1) 

        if len(s1) > len(s2):
            return False
        
        else:
            for s in s1:
                count_1[s] = count_1.get(s, 0) + 1
            
            for t in range(l, r):
                count_2[s2[t]] = count_2.get(s2[t], 0) + 1

            while r <= len(s2):

                if count_1 == count_2:
                    return True
                    
                if r == len(s2):
                    return False
         
                count_2[s2[l]] -= 1
                if count_2[s2[l]] == 0:
                    del count_2[s2[l]]
                count_2[s2[r]] = count_2.get(s2[r], 0) + 1

                l += 1
                r += 1


            return False


