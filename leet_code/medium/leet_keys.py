class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        need = [i for i in range(len(rooms))]
        visited = []
        found = [0]
        
        def traverse(r):
            if r not in visited:
                visited.append(r)

            for j in range(len(rooms[r])):
                if rooms[r][j] not in found:
                    found.append(rooms[r][j])
                    traverse(rooms[r][j])
        
        traverse(0)
        
        return sorted(found) == need


#https://leetcode.com/problems/keys-and-rooms/