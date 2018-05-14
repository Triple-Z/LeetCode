class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        para_stack = list()
        for char in s:
            if char in ('(', '{', '['):
                para_stack.append(char)
            elif char in (')', '}', ']'):
                para_pair = {
                    ')': '(',
                    '}': '{',
                    ']': '[',
                }.get(char)
                if len(para_stack) > 0 and para_stack[-1] == para_pair:
                    print(para_stack[-1])
                    para_stack.pop()
                else:
                    return False
            else:
                return False
        
        if len(para_stack) == 0:
            return True
        else:
            return False
