class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        paths = []

                                
        for i in range(len(graph)):
            if not paths:
                for j in range(len(graph[i])):
                    paths.append([i,graph[i][j]])
            else:
                total = sum(1 for path in paths if i in path and graph[i]) 
                p = 0
                temp = []
                while p < len(paths):
                    if i in paths[p] and total:
                        for j in range(len(graph[i])):
                            temp_path = list(paths[p])
                            temp_path.append(graph[i][j])
                            temp.append(temp_path)
                        paths.pop(p)
                        p -= 1
                        total -= 1
                    p += 1
                if temp:
                    paths.extend(temp)
            
        return paths
                       

#https://leetcode.com/problems/all-paths-from-source-to-target/