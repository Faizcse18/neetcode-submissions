class Solution:
    def isValid(self, s: str) -> bool:
        faiz={")":"(","}":"{","]":"["}
        
        stack=[]

        for c in s:
            if c in faiz:
                if stack and stack[-1]==faiz[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)
        return True if not stack else False
        