# 1. 진입 차수가 0인 정점을 큐에 삽입한다.
# 2. 큐에서 원소를 꺼내 해당 원소에 연결된 간선을 제거한다.
# 3. 간선을 제거한 후 진입 차수가 0이 된 정점을 큐에 삽입한다.
# 4. 위 과정을 반복한다.

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    answer = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        answer.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
