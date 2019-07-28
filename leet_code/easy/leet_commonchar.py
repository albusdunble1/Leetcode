class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        bool_list = []
        output = []
        
        for i in range(len(A[0])):
            bool_list = []
            for j in range(1, len(A)):
                # print("A[0][i] = " + A[0][i])
                # print("i = " + str(i))
                if A[0][i] in A[j]:
                    bool_list.append(True)
                    # print("true")
                else:
                    bool_list.append(False)
                    # print("false")
            
            if all(bool_list):
                output.append(A[0][i])
                # print(output)
                
                for k in range(1, len(A)):
                    A[k] = A[k].replace(A[0][i],'', 1)
                    # print("A[k] after replacing = " + A[k] + ", A[0][i] = " + A[0][i])
        
        return output

#         not my solution (very efficient)

#         for i in range(len(A[0])):
#             bool_list = []
#             flag = True
#             for j in range(1, len(A)):
#                 if A[0][i] not in A[j]:
#                     flag = False
#                     break
#                 else:
#                     A[j] = A[j].replace(A[0][i],'', 1)
            
#             if flag:
#                 output.append(A[0][i])                
        
#         return output
                    

#https://leetcode.com/problems/find-common-characters/