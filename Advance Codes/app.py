from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize game state
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/move', methods=['POST'])
def move():
    global current_player
    data = request.json
    row, col = data['row'], data['col']

    if board[row][col] == ' ':
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            return jsonify({'status': 'win', 'winner': winner, 'board': board})
        if all(cell != ' ' for row in board for cell in row):
            return jsonify({'status': 'draw', 'board': board})
        current_player = 'O' if current_player == 'X' else 'X'
    else:
        return jsonify({'status': 'invalid', 'board': board})

    return jsonify({'status': 'ok', 'board': board})

if __name__ == '_main_':
    app.run(debug=True)