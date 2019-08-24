class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ''
        
        minimum = min([len(s) for s in strs])
        
        output = ''
        
        i = 0
        ref_word = strs[0]
        while i < minimum:
            if all(True if strs[j][i] == ref_word[i] else False for j in range(len(strs))):
                output += ref_word[i]
            else:
                break
            
            i += 1
        
        return output


        # sometimes faster solution (also mine)

        # if not strs:
        #     return ''
        
        # sample = strs[0] if strs else ''
        # minimum = min([len(s) for s in strs])

        # counter = 0
        
        # for i in range(minimum):
        #     same = True
        #     for j in range(1,len(strs)):
        #         if sample[i] != strs[j][i]:
        #             same = False
        #             break
            
        #     if same:
        #         counter += 1
        #     else:
        #         break
            
        # if counter:
        #     return sample[:counter:]
        # return ''
        

#https://leetcode.com/problems/longest-common-prefix/