class Solution:
    def isValid(self, s: str ) -> bool:
      
        if s == '':
            return False
        if len(s) == 1:
            return False


        

        stack = []
        s = list(s)
        

        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '[' or s[i] == '{'  :
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                tmp = stack[-1]
                if tmp == '(':
                    if s[i] == ')':
                        stack.pop()
                    else:
                        return False
                elif tmp == '[':
                    if s[i] == ']':
                        stack.pop()
                    else:
                        return False
                elif tmp == '{':
                    if s[i] == '}':
                        stack.pop()
                    else:
                        return False

        # print(True if len(stack) == 0 else False)
        return True if len(stack) == 0 else False
        