import sys

def is_bipartite(graph, start, visited, color):
    stack = [(start, 0)]
    visited[start] = True
    color[start] = 0

    while stack:
        current, current_color = stack.pop()

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                color[neighbor] = 1 - current_color
                stack.append((neighbor, 1 - current_color))
            elif color[neighbor] == current_color:
                return False

    return True

def find_roads(N, M, edges):
    graph = {i: [] for i in range(1, N+1)}

    for edge in edges:
        city1, city2 = edge
        graph[city1].append(city2)
        graph[city2].append(city1)

    visited = [False] * (N + 1)
    color = [-1] * (N + 1)

    for i in range(1, N + 1):
        if not visited[i]:
            if not is_bipartite(graph, i, visited, color):
                print("Nelze")
                return

    group1 = [i for i in range(1, N + 1) if color[i] == 0]
    group2 = [i for i in range(1, N + 1) if color[i] == 1]

    print(" ".join(map(str, group1)))
    print(" ".join(map(str, group2)))

def main():
    edges = []
    N = int(input())
    M = int(input())

    if M == 0:
        print('Nelze')
    else:
        for _ in range(M):
            line = input().split()
            line = list(map(int, line))
            edges.append(line)
        find_roads(N, M, edges)

if __name__ == "__main__":
    main()
