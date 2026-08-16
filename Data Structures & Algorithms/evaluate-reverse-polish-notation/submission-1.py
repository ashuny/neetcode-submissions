class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:

            if t not in "+-*/":
                stack.append(int(t))
            else:
                if t == '+':
                    x = stack.pop() + stack.pop()
                elif t == '-':
                    a = stack.pop()
                    b = stack.pop()
                    x = int(b - a)
                elif t == '*':
                    x = stack.pop() * stack.pop()
                else:
                    a = stack.pop()
                    b = stack.pop()
                    x = int(b / a)
                
                stack.append(x)
            
        return stack[-1]
            
