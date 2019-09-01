class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

#         original solution (time limit exceeded)

#         s = list(s)
#         v = "aeiouAEIOU"
#         end = len(s)-1
#         visited = []
#         mapping = {}
#         order = []
        
#         for i in range(len(s)):
#             if s[i] in v and i not in visited:
#                 visited.append(i)
#                 for j in range(end, -1, -1):
#                     if i == j:
#                         return ''.join(s)
#                     else:
#                         if s[j] in v and j not in visited: 
#                             visited.append(j)
#                             # print(i,j,s[i],s[j])
#                             s[i], s[j] = s[j], s[i]
#                             end = j-1
#                             break
#             elif i in visited:
#                 break
                
        
#         return ''.join(s)
    
# ==================================================================        

#       second solution

        s = list(s)
        v = "aeiouAEIOU"
        mapping = {}
        order = []
    
        for i in range(len(s)):
            if s[i] in v:
                mapping[i] = s[i]
                order.append(i)
        
        rorder = order[::-1]
        for i in range(len(order)):
            s[order[i]] = mapping[rorder[i]]
        
        return ''.join(s)