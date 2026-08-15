class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')' : '(', '}' : '{', ']' : '['} 
        stack = []

        for r in s:
            if r in pair:
                if stack and pair[r] == stack[-1]:
                    stack.pop()
                else: 
                    return False

            else: 
                stack.append(r)
                
            
        return True if not stack else False
        
