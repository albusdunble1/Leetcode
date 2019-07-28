class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """

        extra = 1
        output = []
        while candies > 0:
            for j in range(num_people):
                idx = j+1
                if len(output) >= idx:
                    if candies > extra:
                        output[j] += extra
                        candies -= extra
                    else:
                        output[j] += candies
                        candies = 0
                else:
                    if candies > extra:
                        output.append(extra)
                        candies -= extra
                    else:
                        output.append(candies)
                        candies = 0
                extra += 1

        return output


#https://leetcode.com/problems/distribute-candies-to-people/


