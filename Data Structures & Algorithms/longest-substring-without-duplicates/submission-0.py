class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        mlen = 0
        ss = set()

        while r < len(s):
            if s[r] not in ss:
                ss.add(s[r])
                mlen = max(mlen, len(ss))
                r += 1
            else:
                while s[r] in ss:
                    ss.remove(s[l])
                    l += 1
        
        return mlen


            
