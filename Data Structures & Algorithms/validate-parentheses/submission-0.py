class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {')':'(', ']':'[','}':'{'}

        for char in s:
            if char in bracketMap:
                if len(stack) > 0 and stack[-1] == bracketMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) > 0:
            return False

        return True