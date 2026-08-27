class Solution:
    def isValid(self, s: str) -> bool:
        same = { ")" : "(", "}" : "{", "]" : "["}
        stack = []

        for ch in s:
            if ch in same:
                if not stack or same[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0