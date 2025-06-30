def dfs_water_jug():
    visited = set()
    stack = []
    parent = {}

    start = (0, 0)
    stack.append(start)
    visited.add(start)
    parent[start] = None

    while stack:
        current = stack.pop()
        if is_goal(current):
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("DFS Path to goal:")
            for step in path:
                print(step)
            return

        for state in get_next_states(*current):
            if state not in visited:
                visited.add(state)
                parent[state] = current
                stack.append(state)

    print("No solution found using DFS.")

dfs_water_jug()
