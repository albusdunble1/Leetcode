class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
#         address = address.replace('.', '[.]')
        
#         return address
    
        i = 0
        while i < len(address):
            if address[i] == '.':
                address = address[:i:] + '[' + address[i] + ']' + address[i+1::]
                i += 2
                print(address)
            else:
                i += 1
        return address

#         list_address = list(address)
    
#         i = 0
#         while i < len(list_address):
#             if list_address[i] == '.':
#                 list_address.insert(i,'[')
#                 list_address.insert(i+2,']')
#                 i += 2
#             else:
#                 i += 1
        
#         return ''.join(list_address)


#https://leetcode.com/problems/defanging-an-ip-address/