from guizero import App, Box, PushButton, Text

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board

def check_winner():
    """Check if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

def is_draw():
    """Check if the game is a draw."""
    for row in board:
        if "" in row:
            return False
    return True

def handle_click(row, col, button):
    """Handle a button click."""
    global current_player
    if board[row][col] == "":  # If the cell is empty
        board[row][col] = current_player
        button.text = current_player
        winner = check_winner()
        if winner:
            status_text.value = f"Player {winner} wins!"
            disable_all_buttons()
        elif is_draw():
            status_text.value = "It's a draw!"
            disable_all_buttons()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
            status_text.value = f"Player {current_player}'s turn"

def disable_all_buttons():
    """Disable all buttons on the board."""
    for row in buttons:
        for button in row:
            button.disable()

# GUI setup
app = App("Tic Tac Toe", width=300, height=350)
status_text = Text(app, text="Player X's turn", size=16)

# Create a 3x3 grid of buttons
board_box = Box(app, layout="grid")
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        btn = PushButton(
            board_box,
            text="",
            grid=[col, row],
            width=5,
            height=2,
            command=handle_click,
            args=[row, col, None],  # Updated args
        )
        btn.update_command(handle_click, [row, col, btn])  # Correctly pass the button instance
        button_row.append(btn)
    buttons.append(button_row)

# Run the app
app.display()
