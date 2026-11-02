def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            for i in range(len(graph[node]) -1, -1, -1):
                if graph[node][i] == 1 and i not in visited:
                    stack.append(i)

    return stack
