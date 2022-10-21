import random

board = [[" * ", " * ", " * "],
                [" * ", " * ", " * "],
                [" * ", " * ", " * "]]

#pos of the players in the grid
def listindex(listofelements, element):

    final = []
    y = 0
    
    for i, x, j in listofelements:
        y += 1
        for element in i , x , j:
            if y == 1:
                if i == " * ":
                    pass
                else:
                    indexlist1 = []
                    indexlist1.append(0)
                    indexlist1.append(0)
                    final.append(indexlist1)
                if x == " * ":
                    pass
                else:
                    indexlist1t = []
                    indexlist1t.append(0)
                    indexlist1t.append(1)
                    final.append(indexlist1t)
                if j == " * ":
                    pass
                else:
                    indexlist1t2 = []
                    indexlist1t2.append(0)
                    indexlist1t2.append(2)
                    final.append(indexlist1t2)
                    
            if y == 5:
                if i == " * ":
                    pass
                else:
                    indexlist2 = []
                    indexlist2.append(1)
                    indexlist2.append(0)
                    final.append(indexlist2)
                if x == " * ":
                    pass
                else:
                    indexlist2t = []
                    indexlist2t.append(1)
                    indexlist2t.append(1)
                    final.append(indexlist2t)
                if j == " * ":
                    pass
                else:
                    indexlist2t2 = []
                    indexlist2t2.append(1)
                    indexlist2t2.append(2)
                    final.append(indexlist2t2)
                    
            if y == 9:
                if i == " * ":
                    pass
                else:
                    indexlist3 = []
                    indexlist3.append(2)
                    indexlist3.append(0)
                    final.append(indexlist3)
                if x == " * ":
                    pass
                else:
                    indexlist3t = []
                    indexlist3t.append(2)
                    indexlist3t.append(1)
                    final.append(indexlist3t)
                if j == " * ":
                    pass
                else:
                    indexlist3t2 = []
                    indexlist3t2.append(2)
                    indexlist3t2.append(2)
                    final.append(indexlist3t2)
            y += 1
            
    return final
    
 #Player pos
def playerindex(compare):
    final = []
    choice = ["1", "2", "3"]
    print("Choose 1, 2 or 3")
    while True:
        row = input("Row: ")
        if row in choice: 
        	break
        else:
        	print("Has to be 1, 2 or 3")
    
    print("Choose 1, 2 or 3")
    while True:
        line = input("Line: ")
        if line in choice:
        	break
        else: 
        	print("Has to be: 1, 2 or 3. ")
        
    final.append(int(row) -1)
    final.append(int(line)-1)
    print()
    return final if final not in compare else playerindex(compare)
    
#Bot pos
def botindex(compare):
    final = []
    row = random.randint(0,2)
    line = random.randint(0,2)
    final.append(row)
    final.append(line)
    return final if final not in compare else botindex(compare)

#Check to see if there is a winner
def checkwinfunction(board):
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " * " and board[i][1] != " * " and board[i][2] != " * ":
            return True
            break
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " * " and board[1][i] != " * " and board[2][i] != " * ":
            return True
            break
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " * " and board[1][1] != " * " and board[2][2] != " * ":
            return True
            break
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " * " and board[1][1] != " * " and board[2][0] != " * ":
            return True
            break
        if i == 2 and " * " not in board[0] and " * " not in board[1] and " * " not in board[2]:
            return "Tie"
            break
            
#Print the board
def printboard(board):
    
    print(board[0])
    print(board[1])
    print(board[2])
    print()
    
#Choose to play against bot or another player
playerselectlist = ["Player", "player", "p", "Bot", "bot", "b"]
botlist = ["Bot", "bot", "b"]

while True:
    playerselect = input("Play Against: Player or Bot? ")
    print()
    if playerselect in playerselectlist:
        break
    else:
        print("Choose: Player or Bot.")
 
#Choose to play as x or o             
while True:
    if playerselect in botlist:
        userinput = input("Play as: x or o? ")
    else:
        userinput = input("Player 1 as: x or o? ")
    if userinput == "x":
        userinput = " x "
        player2 = " o "
        break
    elif userinput == "o":
        userinput = " o "
        player2 = " x "
        break
    
element = userinput, player2
print()

#Game loop
while True:
    
    if playerselect in botlist:
        print("Your turn:")
    else:
        print("Player 1's turn:")
        
    indexlist = listindex(board, element)
    playercompare = playerindex(indexlist)
    board[playercompare[0]][playercompare[1]] = userinput
    printboard(board)
    checkwin = checkwinfunction(board)
    
    if checkwin or checkwin == "Tie":
        if checkwin == "Tie":
            print("Game Over. It's a Tie!")
            break
        elif playerselect in botlist:
            print("Game Over. You win.")
            break
        else:
            print("Game Over. Player 1 wins.")
            break
        
    indexlist = listindex(board, element)
    
    if playerselect in botlist:
        print("Bot's turn:")
        botcompare = botindex(indexlist)
        board[botcompare[0]][botcompare[1]] = player2
    else:
        print("Player 2's turn:")
        playercompare = playerindex(indexlist)
        board[playercompare[0]][playercompare[1]] = player2
        
    printboard(board)
    checkwin = checkwinfunction(board)
    
    if checkwin or checkwin == "Tie":
        if checkwin == "Tie":
            print("Game Over. It's a Tie!")
            break
        elif playerselect in botlist:
            print("Game Over. Bot wins.")
            break
        else:
            print("Game Over. Player 2 wins.")
            break
