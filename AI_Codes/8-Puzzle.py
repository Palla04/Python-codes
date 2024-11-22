import heapq

# Directions for moving the blank space (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_empty_tile(state):
    """Find the position of the empty tile (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def is_valid_move(x, y):
    """Check if a move is within the bounds of the puzzle."""
    return 0 <= x < 3 and 0 <= y < 3

def get_possible_moves(state):
    """Generate all possible states by moving the empty tile."""
    x, y = get_empty_tile(state)
    possible_moves = []
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y):
            new_state = [row[:] for row in state]  # Copy the state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            possible_moves.append(new_state)
    
    return possible_moves

def h1(state):
    """Heuristic h1: Always 0."""
    return 0

def h2(state, goal_state):
    """Heuristic h2: Number of misplaced tiles."""
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                misplaced += 1
    return misplaced

def h3(state, goal_state):
    """Heuristic h3: Sum of Manhattan distances of tiles."""
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = (value - 1) // 3, (value - 1) % 3
                total_distance += abs(i - goal_x) + abs(j - goal_y)
    return total_distance

def h4(state, goal_state):
    """Heuristic h4: A heuristic that's guaranteed to be greater than optimal."""
    return h2(state, goal_state) + h3(state, goal_state) + 1  # Combination of h2 and h3, intentionally overestimating

def a_star(initial_state, goal_state, heuristic):
    """A* search algorithm to solve the 8-puzzle."""
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(initial_state, goal_state), 0, initial_state, []))  # (f, g, state, path)
    closed_list = set()
    seen_states = set()

    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)
        
        # If we reach the goal state
        if current_state == goal_state:
            return path + [current_state]
        
        # Add to closed list
        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in seen_states:
            continue
        seen_states.add(state_tuple)

        # Generate possible moves
        for next_state in get_possible_moves(current_state):
            new_g = g + 1  # Cost to reach next state is always 1 (one move)
            f_cost = new_g + heuristic(next_state, goal_state)  # f = g + h
            heapq.heappush(open_list, (f_cost, new_g, next_state, path + [current_state]))
    
    return None  # No solution found

def print_puzzle(state):
    """Utility to print the state of the puzzle."""
    for row in state:
        print(" ".join(str(x) for x in row))
    print()

if __name__ == "__main__":
    # Input initial state
    print("Enter the initial state of the puzzle (3 rows of 3 numbers, separated by spaces):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)

    # Input goal state
    print("Enter the goal state of the puzzle (3 rows of 3 numbers, separated by spaces):")
    goal_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        goal_state.append(row)

    # Input heuristic choice
    print("Choose a heuristic (1-4):")
    print("1. h1(n) = 0")
    print("2. h2(n) = Number of misplaced tiles")
    print("3. h3(n) = Sum of Manhattan distances")
    print("4. h4(n) = Combination of h2 and h3 (overestimating)")
    
    choice = int(input().strip())

    heuristics = [h1, h2, h3, h4]

    # Run the A* algorithm with the chosen heuristic
    solution = a_star(initial_state, goal_state, heuristics[choice - 1])

    # Output the solution
    if solution:
        print("Solution found:")
        for step in solution:
            print_puzzle(step)
    else:
        print("No solution found.")
