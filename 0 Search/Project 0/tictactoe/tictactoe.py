"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    print("-----------------------------------------------")
    print("initial_state_START")
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    print("-----------------------------------------------")
    print("player_START")
    sum_X = 0
    sum_O = 0
    sum_EMPTY = 0

    for row in board:
        for cell in row:
            match cell:
                case 'X':
                    sum_X += 1
                case 'O':
                    sum_O += 1
                case None:
                    sum_EMPTY +=1
      
    if (sum_EMPTY == 9): return X
    elif sum_X <= sum_O:  return X
    else: return O
  

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    print("-----------------------------------------------")
    print("actions_START")
    actions = set()
    for (i, row) in enumerate(board):
            #print(row)
            for (j, cell) in enumerate(row):
                if cell == None: actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("-----------------------------------------------")
    print("result_START: \n", board, action)
    possible_actions = actions(board)
    print("Actions: \n", possible_actions)

    next_player = player(board)
    print("player: ", next_player)

    if action not in possible_actions: raise Exception

    new_board = copy.deepcopy(board)

    new_board[action[0]][action[1]] = next_player
    print("result_board: \n", board)
    print("result_new_board: \n", new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    print("-----------------------------------------------")
    print("winner_START")
    #rows
    for (i, row) in enumerate(board):
            if len(set(row)) == 1: return row[0]

    #columns       
    for j in (0,1,2):
        if len(set((board[0][j], board[1][j], board[2][j]))) == 1: return board[0][j]

    #diag
    if len(set((board[0][0], board[1][1], board[2][2]))) == 1: return board[0][0]
    if len(set((board[0][2], board[1][1], board[2][0]))) == 1: return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    print("-----------------------------------------------")
    print("terminal_START")
    if winner(board): return True
    if len(actions(board)) == 0: return True
    print("terminal_FALSE with board: \n", board)
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    print("-----------------------------------------------")
    print("utility_START: ", board)
    winner_player = winner(board)
    print("utility_Winner: ", winner_player)
    if winner_player == X: return 1
    if winner_player == O: return -1
    
    return 0


pos_inf = float('inf')
print('Positive Infinity:', pos_inf)

neg_inf = float('-inf')
print('Negative Infinity:', neg_inf)

def maxvalue(board, level):
    print("-----------------------------------------------")
    print("maxvalue_START", board)
    print("LEVEL: ", level)
    level += 1
    if terminal(board):
        return utility(board)
    v = neg_inf
    for action in actions(board):
        action_result = result (board, action)
        result_v = minvalue(action_result, level)
        v = max(v, result_v)

    return v 

def minvalue(board, level):
    print("-----------------------------------------------")
    print("minvalue_START: ", board)
    print("LEVEL: ", level)
    level += 1
    if terminal(board):

        return utility(board)
    v = pos_inf
    for action in actions(board):
        action_result = result (board, action)
        result_v = maxvalue(action_result, level)
        v = min(v, result_v)
    
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("-----------------------------------------------")
    print("minimax_START")
    level = 0

    optimal_action = None
    if terminal(board): 
        print("minimax_Terminal!")
        return None
    if player(board) == X:
        print("minimax_Player: ", X)
        v = neg_inf
        for action in actions(board):
            print("minimax_Action: ", action)
            action_result = result (board, action)
            result_v = minvalue(action_result,level)
            if result_v > v:
                optimal_action = action
                v = result_v
    else:
        print("minimax_Player: ", O)
        v = pos_inf
        for action in actions(board):
            print("minimax_Action: ", action)
            action_result = result (board, action)
            result_v = maxvalue(action_result, level)
            if result_v < v:
                optimal_action = action
                v = result_v
    
    return optimal_action  
