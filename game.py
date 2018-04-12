# Made by Himanshu Patel
# www.himanshuptl.me

import copy
board = [['-', '-', '-', '-', '-', '-', '-', '-', ], ['-', '-', '-', '-', '-', '-', '-', '-', ],
         ['-', '-', '-', '-', '-', '-', '-', '-', ], ['-', '-', '-', 'w', 'b', '-', '-', '-', ],
         ['-', '-', '-', 'b', 'w', '-', '-', '-', ], ['-', '-', '-', '-', '-', '-', '-', '-', ],
         ['-', '-', '-', '-', '-', '-', '-', '-', ], ['-', '-', '-', '-', '-', '-', '-', '-', ]]
ini = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n = 8
depth = 2
result = []
found = 0
def printtab():
    for i in range(len(board)):
        if i == 0:
            print(""),
            for j in range(len(ini)):
                print("   ", j, end="")
            print("")
        print(str(i) + ' ' + str(board[i]))


def change(abc, row, col):
    val = abc[row][col]
    if val == 'w':
        val = 'b'
    else:
        val = 'w'
    abc[row][col] = val

def move(x,y,j):
    global board, found, result
    abc = copy.deepcopy(board)
    # print("Result :", result)
    for b in result:
        if found > 0:
            change(abc, b[0], b[1])
    abc[x][y] = player[j]
    found = 0
    result = []
    return abc

def Validmove(row, col, j):
    global board, ini, result, found
    tmp = []
    # result = []
    if j == 0:
        m = 1
    else:
        m = 0
    len = range(row - 1, row + 2)
    if board[row][col] != '-':
        return False
    for i in len:
        for k in range(col - 1, col + 2):
            if i < 8 and k < 8:
                if board[i][k] == player[m]:
                    pos = [i, k]
                    tmp.append(pos)
    # print(tmp)
    for d in tmp:
        if d[0] == row:
            y = d[1]
            for a in range(8):
                if y > col:
                    y = y + 1
                else:
                    y = y - 1

                if y < 8 and board[row][y] == player[m]:
                    tmp.append([row, y])
                elif y < 8 and board[row][y] == player[j]:
                    result.append(d)
                    found += 1
                    # print("Result12:", result)
                    break
                else:
                    break
        elif d[1] == col:
            x = d[0]
            for a in range(8):

                if x > row:
                    x = x + 1
                else:
                    x = x - 1
                if x < 8 and board[x][col] == player[m]:
                    tmp.append([x, col])
                elif x < 8 and board[x][col] == player[j]:
                    result.append(d)
                    found += 1
                    # print("Result12:",result)
                    break
                else:
                    break
        else:
            # print("oh")
            x = d[0]
            y = d[1]
            for a in range(8):

                if x > row:
                    x = x + 1
                    if y > col:
                        y = y + 1
                    else:
                        y = y - 1
                else:
                    x = x - 1
                    if y > col:
                        y = y + 1
                    else:
                        y = y - 1
                # print(x,y,j)
                if x < 8 and y < 8 and board[x][y] == player[m]:
                    tmp.append([x, y])
                elif x < 8 and y < 8 and board[x][y] == player[j]:
                    result.append(d)
                    found += 1
                    # print("Result12:", result)
                    break
                else:
                    break

    if found == 0:
        # print("Wrong move")
        return False
    # return 0
    else:
        # board[row][col] = player[j]
        # printtab()
        return True
    # return 1

def IsTerminalNode(board, player):
    for y in range(n):
        for x in range(n):
            if Validmove(x, y, player):
                return False
    return True

minEvalBoard = -1 # min - 1
maxEvalBoard = n * n + 4 * n + 4 + 1 # max + 1
def EvalBoard(board, player):
    tot = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == player:
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
                    tot += 4 # corner
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
                    tot += 2 # side
                else:
                    tot += 1
    return tot
player = ['w', 'b']
j = 0
def BestMove(board, player):
    maxPoints = 0
    mx = -1; my = -1
    for x in range(n):
        for y in range(n):
            if Validmove(x, y, player):
                boardTemp = move(x, y, player)
                points = Minimax(boardTemp, player, depth, True)
                if points > maxPoints:
                    maxPoints = points
                    mx = x; my = y
    return (mx, my)
def Minimax(board, player, depth, maximizingPlayer):
    if depth == 0 or IsTerminalNode(board, player):
        return EvalBoard(board, player)
    if maximizingPlayer:
        bestValue = minEvalBoard
        for y in range(n):
            for x in range(n):
                if Validmove(x, y, player):
                    boardTemp = move(x,y,player)
                    v = Minimax(boardTemp, player, depth - 1, False)
                    bestValue = max(bestValue, v)
    else: # minimizingPlayer
        bestValue = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if Validmove(x, y, player):
                    boardTemp = move(x, y, player)
                    v = Minimax(boardTemp, player, depth - 1, True)
                    bestValue = max(bestValue, v)
    return bestValue
def check():
    global board
    count = 0
    a, b = 0, 0
    for i in range(len(board)):
        if '-' in board[i]:
            count += 1

    if count == 0:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == player[0]:
                    a += 1
                else:
                    b += 1

        printtab()
        if a > b:
            print("Player w Wins")
            exit()
        elif a == b:
            print("Tie")
            exit()
        else:
            print("Player b Wins")
            exit()

print("Enter a Option")
print("1. Human vs Human")
print("2. Human vs AI")
print("3. AI vs AI")
ch = int(input())
printtab()
while True:
    # col = ini.index(col)
    # print(row,col)
    # while mv != 0:
    for j in range(2):
        if (j ==0 and ch == 1) or (j ==1 and ch == 1) or (j ==0 and ch == 2):   # User Move
            valid = 0
            while valid == 0:
                print("Enter a Move for :", player[j])
                row, col = map(str, input().split())
                row, col = int(row), int(col)
                # row, col = 2, 4
                #valid = move(int(row), int(col), int(j))
                if Validmove(row, col, j):
                    valid = 1
                    board = move(row, col, j)
                    check()
                else:
                    print("Wrong Move")
        elif (j ==0 and ch == 3) or (j ==1 and ch == 3) or (j ==1 and ch == 2): # AI's Move
            (x, y) = BestMove(board, j)
            if not (x == -1 and y == -1):
                if Validmove(x, y, j):
                    board = move(x, y, j)
                    check()
        printtab()


