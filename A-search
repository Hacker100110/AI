import heapq

def misplaced_tiles(state, goal):
    return sum(state[i][j] != goal[i][j] and state[i][j] != 0 for i in range(3) for j in range(3))

def get_neighbors(state):
    x, y = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]
    moves = {'Up': (-1, 0), 'Down': (1, 0), 'Left': (0, -1), 'Right': (0, 1)}
    neighbors = []
    for move, (dx, dy) in moves.items():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [r[:] for r in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((move, new_state))
    return neighbors

def a_star_search(initial, goal):
    heap = []
    h = misplaced_tiles(initial, goal)
    heapq.heappush(heap, (h, 0, h, initial, []))
    visited = set()

    while heap:
        f, g, h, state, path = heapq.heappop(heap)
        state_tuple = tuple(map(tuple, state))
        if state == goal:
            return path, g, misplaced_tiles(initial, goal), g + misplaced_tiles(initial, goal)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for move, neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                new_g = g + 1
                new_h = misplaced_tiles(neighbor, goal)
                heapq.heappush(heap, (new_g + new_h, new_g, new_h, neighbor, path + [(move, neighbor, new_g, new_h)]))
    return None, 0, 0, 0

def print_solution(path, initial, g, h, f):
    p = lambda row: " ".join(str(x) if x else " " for x in row)
    print("Initial State:")
    print(f"g(n): {g} | h(n): {h} | f(n): {f}")
    for row in initial: print(p(row))
    print("\nSolution Steps:")
    for move, state, g, h in path:
        print(f"\nMove: {move} | g(n): {g} | h(n): {h} | f(n): {g + h}")
        for row in state: print(p(row))
    print("\nGoal Reached!")

def read_state(prompt):
    print(prompt)
    return [list(map(int, input(f"Enter row {i+1} : ").split())) for i in range(3)]

initial = read_state("Enter the Initial State :")
goal = read_state("\nEnter the Goal State :")

path, g, h, f = a_star_search(initial, goal)
print_solution(path, initial, g, h, f) if path else print("No solution found.")
