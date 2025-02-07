# Connect 4 Game Program

def initialize_board(board):
    for row in range(6):
        for col in range(7):
            board[row][col] = ' '

def print_board(board):
    print('\n  1   2   3   4   5   6   7')
    print('+---+---+---+---+---+---+---+')
    for row in range(6):
        print('|', end='')
        for col in range(7):
            print(' %s |' % board[row][col], end='')
        print('\n+---+---+---+---+---+---+---+')
    
def board_full(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == ' ':
                return False
    return True

def check_win(board, player):
    # Check horizontal spaces
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # Check vertical spaces
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Check / diagonal spaces
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # Check \ diagonal spaces
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

    return False

def play_again():
    while True:
        play_again = input('\nPlay again? (y/n): ')
        if play_again == 'y' or play_again == 'Y':
            return True
        elif play_again == 'n' or play_again == 'N':
            print('\nThanks for playing!\n')
            return False
        else:
            print('Invalid input. Please enter y or n.')

def play_game():
    board = [[' ' for i in range(7)] for j in range(6)]
    player = '1'
    initialize_board(board)
    while True:
        print_board(board)
        while True:
            col = int(input('Player %s, choose a column: ' % player)) - 1
            if 0 <= col <= 6 and board[0][col] == ' ':
                break
            elif col < 0 or col > 6:
                print('\nInvalid column. Please enter a number between 1 and 7.')
            else:
                print('\nColumn is full. Please choose a different column.')
                
        for row in range(5, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = player
                break
        if check_win(board, player):
            print_board(board)
            print('Player %s wins!' % player)
            break
        elif board_full(board):
            print_board(board)
            print('The game is a tie!')
            break
        if player == '1':
            player = '2'
        else:
            player = '1'
    if play_again():
        play_game()

play_game()