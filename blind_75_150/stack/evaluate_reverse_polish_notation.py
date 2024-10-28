from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            print(stack)
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":

                    stack.append(int(a / b))
        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
sol = Solution()
res = sol.evalRPN(tokens)
print(res)


s = "Evaluate Reverse Polish Notation.py".lower()
ls = s.split(" ")
print("_".join(ls))

