# Source code: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/

# Set player symbol to 'x'; opponent symbol to 'o'
player, opponent = 'x', 'o'
 

# Function will return true if there are moves in the board
# else false if not found any moves left
def isMovesLeft(board):
    # Explore/ visit all cells in the tictactoe board
    for i in range(3):
        for j in range(3) :
            # If there is any cell still empty, return True
            if (board[i][j] == '_'):
                return True
    return False
 
# Function for evaluating the tictactoe game
def evaluate(b) :
    # Check if there are 3 X or O's in a row
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):       
            # If player win, +10 points
            if (b[row][0] == player):
                return 10
            # else return -10 points if player defeated (opponent wins)
            elif (b[row][0] == opponent):
                return -10
 
    # Check if there are 3 X or O's in a column
    for col in range(3) :
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            # If player win, +10 points
            if (b[0][col] == player):
                return 10
            # else return -10 points if player defeated (opponent wins)
            elif (b[0][col] == opponent):
                return -10
    
    # Check if there are 3 X or O's in a diagonal (top left to bottom right)
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        # If player win, +10 points
        if (b[0][0] == player):
            return 10
        # else return -10 points if player defeated (opponent wins)
        elif (b[0][0] == opponent):
            return -10
 
    # Check if there are 3 X or O's in a diagonal (top right to bottom left)
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        # If player win, +10 points
        if (b[0][2] == player) :
            return 10
        # else return -10 points if player defeated (opponent wins)
        elif (b[0][2] == opponent):
            return -10
 
    # If the game results in a draw (none of them won), return +0 point
    return 0
 
# Minimax function
def minimax(board, depth, isMax):
    # Get the score from the evaluation function
    score = evaluate(board)
 
    # If player won, return the score
    if (score == 10):
        return score
 
    # If player lost (opponent win), return the score
    if (score == -10):
        return score
 
    # If the match's result is a draw, return the score
    if (isMovesLeft(board) == False):
        return 0
 
    # Player's move (maximizer)
    if (isMax):  
        # Set a temporary value of best to -1000 
        # which will later be updated with the max value of minimax 
        best = -1000
 
        # Explore/ visit all cells in the tictactoe board
        for i in range(3):        
            for j in range(3) :
              
                # If the cell is empty
                if (board[i][j]=='_'):
                 
                    # Player do their move
                    board[i][j] = player
 
                    # Call minimax function recursively 
                    # max(): choose the max value
                    best = max(best, minimax(board,
                                              depth + 1,
                                              not isMax) )
 
                    # Undo the move
                    board[i][j] = '_'
        return best
 
    # Opponent's move (minimizer)
    else :
        # Set a temporary value of best to 1000 
        # which will later be updated with the min value of minimax 
        best = 1000
 
        # Explore/ visit all cells in the tictactoe board
        for i in range(3) :        
            for j in range(3) :
              
                # If the cell is empty
                if (board[i][j] == '_') :
                 
                    # Opponent do their move
                    board[i][j] = opponent
 
                    # Call minimax function recursively 
                    # min(): choose the min value
                    best = min(best, minimax(board, depth + 1, not isMax))
 
                    # Undo the move
                    board[i][j] = '_'
        return best
 
# Function to find the best move/ optimal solution for the player
def findBestMove(board):
    # Set initial bestValue and bestMove
    bestVal = -1000
    bestMove = (-1, -1)
 
    # Explore/ visit all cells in the tictactoe board, evaluate minimax function for
    # all empty cells. And return the cell with optimal value.
    for i in range(3) :    
        for j in range(3) :
         
            # If the cell is empty
            if (board[i][j] == '_') :
             
                # Player do their move
                board[i][j] = player
 
                # Compute the move in the evaluation function
                moveVal = minimax(board, 0, False)
 
                # Undo the move
                board[i][j] = '_'

                # Update the bestMove if the current move value is more than the best value
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
    
    print("The value of the best Move is :", bestVal)

    return bestMove


# Driver code

# Set the tictactoe board
board = [
    [ '_', '_', '_' ],
    [ 'o', '_', 'x' ],
    [ '_', 'o', '_' ]
]

bestMove = findBestMove(board)
 
print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])