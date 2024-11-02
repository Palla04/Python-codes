import random

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def heuristic_h1(state):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal_state[i][j])

def heuristic_h2(state):
    manhattan_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                manhattan_distance += abs(goal_x - i) + abs(goal_y - j)
    return manhattan_distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def generate_moves(state):
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

def is_goal(state):
    return state == goal_state

def generate_random_state():
    flat_state = list(range(9))
    random.shuffle(flat_state)
    return [flat_state[i:i + 3] for i in range(0, 9, 3)]

def hill_climbing(start_state, heuristic, max_restarts=5):
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
                if is_goal(current_state):
                    output_lines.append("Goal reached!")
                    return output_lines
                break

            current_state = next_state
            steps += 1

        current_state = generate_random_state()
        output_lines.append("Stuck in local minimum, restarting...\n")

    return output_lines

def get_initial_state(input_filename):
    with open(input_filename, 'r') as f:
        lines = f.readlines()
    return [list(map(int, line.split())) for line in lines]

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    heuristic_choice = input("Choose heuristic (h1 for misplaced tiles, h2 for Manhattan distance): ")
    heuristic = heuristic_h1 if heuristic_choice == "h1" else heuristic_h2

    start_state = get_initial_state(input_filename)
    output_lines = hill_climbing(start_state, heuristic)

    with open(output_filename, 'w') as f:
        f.write('\n'.join(output_lines))
        f.write("\nFinal state:\n")
        for row in start_state:
            f.write(' '.join(map(str, row)) + "\n")

if __name__ == "__main__":
    main()
