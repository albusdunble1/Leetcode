

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        # parens = [val for val in S]
        
        new_parens = ""
        
        layers = 0
        outer_start = 0
        outer_end = 0
        start_found = False
        end_found = False
        
        for i in range(0,len(S)):
            if i != len(S) - 1:
                if S[i] == "(" and S[i+1] == "(":
                    layers += 1
                    if not start_found:
                        start_found = True
                        outer_start = i
                    
                elif S[i] == ")" and S[i+1] == ")":
                    if  start_found and not end_found:
                        outer_end = i
                        temp = 0
                        for num in range(0,layers):
                                outer_end += 1
                                if S[outer_end] == ")":
                                    temp += 1
                        if layers == temp:
                            end_found = True
                        else:
                            layers -= 1



            if start_found and end_found:
                new_parens += S[outer_start+1:outer_end:]
                start_found = False
                end_found = False
                layers = 0
            
            
                
        return new_parens

solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))

