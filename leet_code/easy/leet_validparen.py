class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         original solution (trial and error)

#         count = 0        
#         opening = ['(','[', '{']
#         closing = [')',']', '}']
#         # Last In First Out
#         lifo = []
        
#         if not s:
#             return True
#         elif s[0] not in opening:
#             return False
        
#         for i in range(len(s)):
#             if s[i] in opening and i != len(s)-1:
#                 if s[i] == '(' and s[i+1] != ']' and s[i+1] != '}':
#                     count += 1
#                     lifo.append(s[i])
#                 elif s[i] == "[" and s[i+1] != ')' and s[i+1] != '}':
#                     count += 1
#                     lifo.append(s[i])
#                 elif s[i] == '{' and s[i+1] != ']' and s[i+1] != ')':
#                     count += 1
#                     lifo.append(s[i])
#                 else:
#                     return False
#             elif s[i] in closing:
#                 if s[i] == ')' and count:
#                     compare = lifo.pop()
#                     if compare == '(':
#                         count -= 1
#                     else:
#                         return False
#                 elif s[i] == "]" and count:
#                     compare = lifo.pop()
#                     if compare == '[':
#                         count -= 1
#                     else:
#                         return False
#                 elif s[i] == '}' and count:
#                     compare = lifo.pop()
#                     if compare == '{':
#                         count -= 1
#                     else:
#                         return False
#                 else:
#                     return False
#             else:
#                 return False
        
#         if not count:
#             return True
#         return False

# ========================================================================================================================
#       refactored solution

        count = 0
        maps = {')':'(', ']':'[', '}':'{'}
        lifo = []
        
        for i in range(len(s)):
            if s[i] not in maps:
                count += 1
                lifo.append(s[i])
            else:
                if lifo:
                    temp = lifo.pop()
                    if maps[s[i]] == temp:
                        count -= 1
                    else:
                        return False
                else:
                    return False

        return not count
                    