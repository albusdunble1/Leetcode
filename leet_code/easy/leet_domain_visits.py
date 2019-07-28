class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        temp_arr = []
        output = []
        
        for domain in cpdomains:
            temp_arr = domain.split(' ') # ['9001', 'discuss.leetcode.com']
            
            j = len(temp_arr[1]) -1
            # for j in range(len(temp_arr[1])-1, 0, -1):
            while j >= 0:
                if temp_arr[1][j] == '.':
                    output.append((temp_arr[0], temp_arr[1][j+1::]))
                elif j == 0:
                    output.append((temp_arr[0], temp_arr[1]))
                j -= 1
                
        domain_dict = {}
        
        for count,domain in output:
            if domain not in domain_dict:
                domain_dict[domain] = int(count)
            else:
                domain_dict[domain] += int(count)
                
        return [str(num) + ' ' + dom for dom,num in domain_dict.items()]


#https://leetcode.com/problems/subdomain-visit-count/