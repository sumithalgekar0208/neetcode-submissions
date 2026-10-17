class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_bracket = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in matching_bracket:
                top_element = stack.pop() if stack else "#"
                if top_element != matching_bracket[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack