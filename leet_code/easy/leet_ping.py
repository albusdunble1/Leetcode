class RecentCounter(object):
        def __init__(self):
            self.pings = []

        def ping(self, t):
            """
            :type t: int
            :rtype: int
            """
            self.pings.append(t)
            
            i = 0
            
            while i >= 0:
                if self.pings[i] < t-3000:
                    self.pings.pop(i)
                    i -= 1
                else:
                    break
                i += 1
                
            return len(self.pings)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


#https://leetcode.com/problems/number-of-recent-calls/