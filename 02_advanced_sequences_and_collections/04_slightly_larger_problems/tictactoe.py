import random
import os
INITIAL_MARKER = " "
HUMAN_MARKER = "X"
COMPUTER_MARKER = "O"
MATCH_WIN_ROUNDS = 5
WINNING_LINES = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],  # rows
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],  # columns
    [1, 5, 9],
    [3, 5, 7],  # diagonals
]

def join_or(lst, delimiter=', ', conjunction='or'):
    match len(lst):
        case 0:
            return ""
        case 1:
            return lst[0]
        case 2:
            return f'{lst[0]} {conjunction} {lst[1]}'
    beginning = delimiter.join(str(el) for el in lst[0:-1])
    return f'{beginning}{delimiter}{conjunction} {lst[-1]}'


def display_scores(scores):
    print("*" * 35)
    print(f"Player: {scores['Player']}    |    Computer: {scores['Computer']}")
    print(f'Win {MATCH_WIN_ROUNDS} rounds to win the match!')
    print("*" * 35)

def display_board(board, scores):
    os.system("clear")
    display_scores(scores)
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print("")
    print("     |     |")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print("     |     |")
    print("-----+-----+-----")
    print("     |     |")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print("     |     |")
    print("")

def display_winner(scores):
    winner = get_match_winner(scores)
    print('*' * 35)
    print(f'Player won {scores['Player']}.')
    print(f'Computer won {scores['Computer']}.')
    print("*" * 35)
    if winner == 'Player':
        print('Congratulations! You win the match!')
    else:
        print('Computer wins the match.')


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}


def prompt(message):
    print(f"==> {message}")


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break  # break if it's a valid square
        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def get_at_risk_square(line, board, player_marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(player_marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None


def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    square = None
    for line in WINNING_LINES:
        square = get_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break
    if not square:
        for line in WINNING_LINES:
            square = get_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break
    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


def board_full(board):
    return len(empty_squares(board)) == 0


def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (
            board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER
        ):
            return "Player"
        elif (
            board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER
        ):
            return "Computer"

    return None


def someone_won(board):
    return bool(detect_winner(board))

def get_match_winner(scores):
    for name, score in scores.items():
        if score >= MATCH_WIN_ROUNDS:
            return name
    return None


def play_game(scores):
    board = initialize_board()

    while True:
        display_board(board, scores)

        player_chooses_square(board)
        if someone_won(board) or board_full(board):
            break

        computer_chooses_square(board)
        if someone_won(board) or board_full(board):
            break

    display_board(board, scores)

    if someone_won(board):
            winner = detect_winner(board)
            prompt(f"{winner} won!")
            scores[winner] += 1
    else:
        prompt("It's a tie!")
    input('Press enter to continue.')


def play_match():
    scores = {'Player': 0, 'Computer': 0}
    while True:
        display_scores(scores)
        play_game(scores)
        if get_match_winner(scores):
            break
    display_winner(scores)

def play_tictactoe():
    while True:
        play_match()
        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != "y":
            break
    prompt("Thanks for playing Tic Tac Toe!")

play_tictactoe()
