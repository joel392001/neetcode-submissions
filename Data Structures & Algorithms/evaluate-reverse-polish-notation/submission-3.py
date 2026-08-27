class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            
            if ch in {'+', '-', '*', '/'}:
                second = stack.pop()
                first = stack.pop()

                if ch == "+":
                    stack.append((first + second))
                elif ch == "-":
                    stack.append((first - second))
                elif ch == "*":
                    stack.append((first * second))
                else:
                    stack.append(int(first / second))

            else:
                stack.append(int(ch))
        return stack[0]
