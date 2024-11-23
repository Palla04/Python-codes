import random
import math

# Define the goal state for the 8-puzzle problem
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 represents the blank tile

# Heuristic: Total Manhattan distance
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find position of blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible moves for the blank tile
def generate_moves(state):
    x, y = find_blank(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append(new_state)
    return moves

# Simulated Annealing algorithm
def simulated_annealing(start_state, max_iterations=1000, temp=1000, cooling_rate=0.95):
    current_state = start_state
    current_heuristic = heuristic(current_state)
    output_lines = []

    for i in range(max_iterations):
        if current_state == goal_state:
            output_lines.append("Goal state reached!")
            break

        next_state = random.choice(generate_moves(current_state))
        next_heuristic = heuristic(next_state)

        # Accept or reject the move based on simulated annealing probability
        delta = next_heuristic - current_heuristic
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_state = next_state
            current_heuristic = next_heuristic

        # Log the current state and heuristic
        output_lines.append(f"Step {i + 1}, Heuristic: {current_heuristic}")
        output_lines.append('\n'.join(' '.join(map(str, row)) for row in current_state))
        output_lines.append("")  # Add a blank line for readability

        # Cool down the temperature
        temp *= cooling_rate

    # Final state output
    output_lines.append("Final state:")
    for row in current_state:
        output_lines.append(' '.join(map(str, row)))

    return output_lines

# Main function to run the algorithm
def main():
    print("Enter the initial state of the puzzle row by row (use 0 for the blank tile):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().strip().split()))
        initial_state.append(row)

    final_output = simulated_annealing(initial_state)

    print("\n".join(final_output))

if __name__ == "__main__":
    main()
