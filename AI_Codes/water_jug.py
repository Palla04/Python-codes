from collections import deque

# Define the maximum capacities of the jugs
JUG_A_CAPACITY = 4
JUG_B_CAPACITY = 3
GOAL = 2

# Define the initial state
initial_state = (0, 0)  # Both jugs are initially empty

# Function to perform the BFS to solve the water jug problem
def water_jug_bfs():
    # Queue to store the states, each state includes the jug amounts and the path taken
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()
        
        # If we have reached the goal, return the solution path
        if a == GOAL or b == GOAL:
            return path + [(a, b)]
        
        # Mark the state as visited
        if (a, b) in visited:
            continue
        visited.add((a, b))

        # Generate all possible next states
        next_states = [
            ((JUG_A_CAPACITY, b), "Fill Jug A"),            # Fill Jug A
            ((a, JUG_B_CAPACITY), "Fill Jug B"),            # Fill Jug B
            ((0, b), "Empty Jug A"),                        # Empty Jug A
            ((a, 0), "Empty Jug B"),                        # Empty Jug B
            ((a - min(a, JUG_B_CAPACITY - b), b + min(a, JUG_B_CAPACITY - b)), "Pour A -> B"),  # Pour A to B
            ((a + min(b, JUG_A_CAPACITY - a), b - min(b, JUG_A_CAPACITY - a)), "Pour B -> A")   # Pour B to A
        ]

        # Add each next state to the queue if not visited
        for (next_a, next_b), action in next_states:
            if (next_a, next_b) not in visited:
                queue.append(((next_a, next_b), path + [(a, b, action)]))

    # If no solution found
    return None

# Run the function and print the solution
solution = water_jug_bfs()
if solution:
    print("Solution steps:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
