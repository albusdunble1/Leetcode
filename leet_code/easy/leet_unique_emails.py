class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        output = []
        
        for i in range(len(emails)):
            at = emails[i].index('@')
            user = emails[i][:at:]
            address = emails[i][at::]
            
            user = user.replace('.', '')
            
            if user.find('+') != -1:
                plus = user.index('+')
                user = user[:plus:]
            
            output.append(" ".join([user,address]))
        
        
        return len(set(output))
            

#https://leetcode.com/problems/unique-email-addresses/