import random

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def heuristic_h1(state):
    """Heuristic 1: Count of misplaced tiles."""
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                misplaced += 1
    return misplaced


def heuristic_h2(state):
    """Heuristic 2: Sum of Manhattan distances."""
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = (value - 1) // 3, (value - 1) % 3
                total_distance += abs(i - goal_x) + abs(j - goal_y)
    return total_distance

def find_blank(state):
    """Find the position of the blank tile (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def generate_moves(state):
    """Generate all possible moves for the blank tile."""
    blank_x, blank_y = find_blank(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            moves.append(new_state)
    return moves

def generate_random_state():
    """Generate a random initial state."""
    flat_state = list(range(9))
    random.shuffle(flat_state)
    return [flat_state[i:i + 3] for i in range(0, 9, 3)]

def hill_climbing(start_state, heuristic, max_restarts=5):
    """Hill climbing algorithm with restarts."""
    output_lines = []
    for restart in range(max_restarts):
        current_state = start_state
        steps = 0

        while True:
            current_heuristic = heuristic(current_state)
            moves = generate_moves(current_state)
            next_state = None
            next_heuristic = float("inf")

            for move in moves:
                move_heuristic = heuristic(move)
                if move_heuristic < next_heuristic:
                    next_state = move
                    next_heuristic = move_heuristic

            output_lines.append(f"Step {steps}: Heuristic Value = {current_heuristic}")
            output_lines.append('\n'.join([' '.join(map(str, row)) for row in current_state]))
            output_lines.append("")

            if next_heuristic >= current_heuristic:
                if current_state==goal_state:
                    output_lines.append("Goal reached!")
                    return output_lines
                break

            current_state = next_state
            steps += 1

        current_state = generate_random_state()
        output_lines.append("Stuck in local minimum, restarting...\n")

    return output_lines


def main():
    heuristic_choice = input("Choose heuristic (h1 for misplaced tiles, h2 for Manhattan distance): ").strip()
    heuristic = heuristic_h1 if heuristic_choice == "h1" else heuristic_h2

    print("Enter the puzzle row wise: ")
    start_state=[]
    for i in range(3):
        row = list(map(int,input().split()))
        start_state.append(row)
            
    output_lines = hill_climbing(start_state, heuristic)

    print("\n".join(output_lines))
    print("Final state:")
    for row in start_state:
        print(*row)

if __name__ == "__main__":
    main()
