class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c for c in s if c.isalnum())
        clean = clean.lower()
        i = 0
        while i < len(clean):
            if clean[i] == clean[len(clean)-i-1]:
                i += 1
            else:
                return False
        return True

        
