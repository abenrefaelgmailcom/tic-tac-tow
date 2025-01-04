
def prepare_board() -> list:
    """מכין לוח משחק ריק לאיקס עיגול"""
    return [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

def draw_board(board):
    """מדפיס את הלוח הנוכחי"""
    for row in board:
        print(" ".join(row))
    print()

def input_location(board):
    """מקבל מיקום לשחקן, כולל בדיקות חוקיות"""
    while True:
        try:
            raw = int(input('Enter Row (0-2): '))
            col = int(input('Enter Column (0-2): '))
            if 0 <= raw <= 2 and 0 <= col <= 2 and board[raw][col] == '_':
                return raw, col
            else:
                print("Invalid input! Choose an empty cell within range 0-2.")
        except ValueError:
            print("Invalid input! Enter numbers between 0 and 2.")

def check_win(board, symbol):
    """בודק האם שחקן מסוים ניצח"""
    # בדיקת שורות
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    # בדיקת עמודות
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    # בדיקת אלכסונים
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def board_is_full(board):
    """בודק אם הלוח מלא"""
    return all(cell != '_' for row in board for cell in row)

# לוגיקת המשחק
counter = 1
board = prepare_board()
draw_board(board)

while True:
    # שחקן X
    print("X's turn:")
    raw, col = input_location(board)
    board[raw][col] = 'X'
    draw_board(board)

    if check_win(board, 'X'):
        print("X won!")
        break
    if board_is_full(board):
        print("It's a tie!")
        break

    # שחקן O
    print("O's turn:")
    raw, col = input_location(board)
    board[raw][col] = 'O'
    draw_board(board)

    if check_win(board, 'O'):
        print("O won!")
        break
    if board_is_full(board):
        print("It's a tie!")
        break
