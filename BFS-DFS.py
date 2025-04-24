def bfs(adj, n, start):
    visited = [False] * n
    q = [start]
    visited[start] = True
    print(f"BFS starting from vertex {start}: ", end="")
    while q:
        v = q.pop(0)
        print(v, end=" ")
        for i in range(n):
            if adj[v][i] and not visited[i]:
                visited[i] = True
                q.append(i)
    print()

def dfs(adj, n, start):
    visited = [False] * n
    print(f"DFS starting from vertex {start}: ", end="")
    def visit(v):
        visited[v] = True
        print(v, end=" ")
        for i in range(n):
            if adj[v][i] and not visited[i]:
                visit(i)
    visit(start)
    print()

def main():
    n = int(input("Enter number of vertices: "))
    print("Enter the adjacency matrix row by row:")
    adj = [list(map(int, input().split())) for _ in range(n)]
    start = int(input("Enter starting vertex for BFS and DFS: "))
    bfs(adj, n, start)
    dfs(adj, n, start)

if __name__ == "__main__":
    main()
