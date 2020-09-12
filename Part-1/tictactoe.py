# Cannot be played continously.

from random import randrange
board =  [' ' for i in range(10)]
def printBoard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+ board[2] + ' | '+board[3]+' ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+board[4]+' | '+ board[5] + ' | '+board[6]+' ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+board[7]+' | '+ board[8] + ' | '+board[9]+' ')
    print('   |   |   ')

def inputLet(l,pos):
    try:
        board[pos] = l
    except TypeError:
        print('Game Tied')
def winner(board,l):
    return((board[1]==l and board[2]==l and board[3]==l)or
    (board[4]==l and board[5]==l and board[6]==l)or
    (board[7]==l and board[8]==l and board[9]==l)or
    (board[1]==l and board[4]==l and board[7]==l)or
    (board[2]==l and board[5]==l and board[8]==l)or
    (board[3]==l and board[6]==l and board[9]==l)or
    (board[1]==l and board[5]==l and board[9]==l)or
    (board[3]==l and board[5]==l and board[7]==l))

def selectRand(lst):
    c = randrange(len(lst))
    return lst[c]

def player():
    run = True
    while(run):
        try:
            move = int(input('Please select a position(1 to 9): '))
            if move > 0 and move < 10:
                if spaceFree(move):
                    run = False
                    inputLet('X',move)
                else:
                    print('Sorry, this space is occupied.')
            else:
                print('Please type a number between 1 and 9')
        except ValueError:
            print('Please enter a valid position')
def computer():
    possible = [i for i,l in enumerate(board) if l == " " and i!=0]
    move = 0
    for c in ['O','X']:
        for x in possible:
            boardcp = board[:]
            boardcp[x] = c
            if winner(boardcp,c):
                move = x
                return move
    cornersFree = []
    for i in possible:
        if i in [1,3,7,9]:
            cornersFree.append(i)
    if len(cornersFree) > 0:
        move = selectRand(cornersFree)
        return move
    
    if 5 in possible:
        move = 5
        return move
    
    edgeFree = []
    for i in possible:
        if i in [2,4,8,6]:
            edgeFree.append(i)
    if len(edgeFree)>0:
        move = selectRand(edgeFree)
        return move

def spaceFree(pos):
    return board[pos] == " "
def boardFull(board):
    if board.count(" ")>1:
        return False
    else:
        return True
def main():
    print('Welcome to TIC-TAC-TOE')
    printBoard(board)
    while(not(boardFull(board))):
        if(not(winner(board,'O'))):
            player()
            printBoard(board)
            print()
        else:
            print('You Lose!')
            break
        if(not(winner(board,'X'))):
            move = computer()
            if move == 0:
                print(" ")
            else:
                inputLet('O',move)
                printBoard(board)
                print()
        else:
            print('You Win!')
            break  


main()
