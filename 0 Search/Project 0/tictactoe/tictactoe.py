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

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
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
    possible_actions = set()
    for (i, row) in enumerate(board):
            #print(row)
            for (j, cell) in enumerate(row):
                if cell == None: possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    possible_actions = actions(board)
    if action not in possible_actions: raise Exception

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #rows
    for row in board:
      if row.count(X) == 3: return X
      if row.count(O) == 3: return O

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
    if winner(board): return True
    if len(actions(board)) == 0: return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X: return 1
    if winner_player == O: return -1
    
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    pos_inf = float('inf')
    neg_inf = float('-inf')

    def maxvalue(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = neg_inf
        for action in actions(board):
            action_result = result (board, action)
            result_v = minvalue(action_result, alpha, beta)
            v = max(v, result_v)
            if alpha >= beta: break # Alpha-Beta Pruning
            alpha = max(alpha, v)
                        
        return v 
    
    def minvalue(board, alpha, beta):
        if terminal(board):
            return utility(board)
        v = pos_inf
        for action in actions(board):
            action_result = result (board, action)
            result_v = maxvalue(action_result, alpha, beta)
            v = min(v, result_v)
            if beta <= alpha: break # Alpha-Beta Pruning
            beta = min(beta, result_v)
            
        return v  
    

    optimal_action = None
    if terminal(board): 
        return None
    
    alpha = neg_inf
    beta = pos_inf

    if player(board) == X:
        
        for action in actions(board):
            action_result = result (board, action)
            result_v = minvalue(action_result, alpha, beta)
            if result_v > alpha:
                optimal_action = action
                alpha = result_v
            
    else:
        
        for action in actions(board):
            action_result = result (board, action)
            result_v = maxvalue(action_result, alpha, beta)
            if result_v < beta:
                optimal_action = action
                beta = result_v
    
    return optimal_action  

