from collections import deque
graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
visited = set()

# 너비우선 탐색
def bfs_iteractive(start_node):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=' ')
            visited.add(node)
            queue.extend(graph[node])


# 깊이 우선탐색
def dfs_iterative(start_node):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node,end='')
            visited.add(node)
            stack.extend(reversed(graph[node]))

snode = 'A'
# 깊이 우선 탐색
print("깊이 우선 탐색")
dfs_iterative(snode)
visited.clear()
print("\n========================")
# 너비우선탐색
print("너비 우선 탐색")
bfs_iteractive(snode)