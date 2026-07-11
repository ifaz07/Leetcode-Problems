from collections import deque

class Solution(object):
    def isBipartite(self, graph):

        n = len(graph)
        colors = [-1] * n         

        for i in range(n):

            if colors[i] != -1:
                continue

            q = deque([i])
            colors[i] = 0

            while q:

                node = q.popleft()

                for nei in graph[node]:

                    if colors[nei] == -1:
                        colors[nei] = 1 - colors[node]
                        q.append(nei)

                    elif colors[nei] == colors[node]:
                        return False

        return True



        