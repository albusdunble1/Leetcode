class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        
        def not_detector(not_expr):
            if not_expr[2] == 't':
                return 'f'
            return 't'
        
        def and_detector(and_expr):
            if 'f' in and_expr:
                return 'f'
            return 't'
        
        def or_detector(or_expr):
            if 't' in or_expr:
                return 't'
            return 'f'
        



# recursion function =========================================

        def extractor_replace(start, end, detector, express):
            # print("start = "+ str(start))
            # print("end = "+ str(end))
            # print("detector = "+ str(detector))
            # print("expression = "+ str(express))
            
            # global global_express
            
            global_express = express
                        
            paren_num = 0
            # print("first pass")
            for i in range(start+1, end):
                
                # print("loop #" + str(i))
                # print("global express = " + global_express)
                # print("expression[i] = " + str(global_express[i]))
                if global_express[i] == '(':
                    # print('( is found')
                    paren_num += 1
                elif global_express[i] == ')':
                    # print(') is found')
                    paren_num -= 1
                elif global_express[i] != ',' and global_express[i] != 't' and global_express[i] != 'f':
                    # print('lol')
                    if global_express[i] == '&':
                        # print("first & recursion")
                        term_tr = extractor_replace(0, len(global_express), and_detector, global_express[i::])
                        global_express = global_express.replace(global_express[i::], term_tr) 
                        # print("replaced, global express = " + global_express)
                    elif global_express[i] == '|':
                        term_tr = extractor_replace(0, len(global_express), or_detector, global_express[i::])
                        global_express = global_express.replace(global_express[i::], term_tr) 
                        # print("replaced, global express = " + global_express)
                    elif global_express[i] == '!':
                        term_tr = extractor_replace(0, len(global_express), not_detector, global_express[i::])
                        global_express = global_express.replace(global_express[i::], term_tr) 
                        # print("replaced, global express = " + global_express)
                
                # print("yoyoyo")
                
                if paren_num == 0:
                    # print("paren_num is 0")
                    # print(global_express[start:i+1])
                    result = detector(global_express[start:i+1])
                    # print("result = " + result )
                    # e.g: replace "|(t,f)" with "t"
                    global_express = global_express.replace(global_express[start:i+1], result) 
                    # print("final expression = " + global_express)
                    break
            return global_express

# recursion function =========================================
        
        if expression[0] == '&':
            answer = extractor_replace(0,len(expression), and_detector, expression)
        elif expression[0] == '|':
            answer = extractor_replace(0,len(expression), or_detector, expression)
        else:
            answer = extractor_replace(0,len(expression), not_detector, expression)
        
        
        if answer == 't':
            return True
        return False
                

#https://leetcode.com/problems/parsing-a-boolean-expression/