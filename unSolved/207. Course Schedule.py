from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ans = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for nextCourse in graph[current]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return len(ans) == numCourses

answer = Solution().canFinish(2, [[1,0],[0,1]])
print("answer", answer)
