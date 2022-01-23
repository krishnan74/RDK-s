board = ['_','_','_',
         '_','_','_',
         '_','_','_']
def board_display():
    print("    "+board[0]+'|'+board[1]+'|'+board[2])
    print("    "+board[3]+'|'+board[4]+'|'+board[5])
    print("    "+board[6]+'|'+board[7]+'|'+board[8])
run = True
count = 0
Check_corner=[1,3,7,9]
Check_tie_list = []

def checkrow():
    global run
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        run = False
    if row1:
        if board[0]=='O':
            print("1st player won the game")
        else:
            print("2nd player won the game")
    if row2:
        if board[3]=='O':
            print("1st player won the game")
        else:
            print("2nd player won the game")
    if row3:
        if board[6]=='O':
            print("1st player won the game")
        else:
            print("2nd player won the game")
    return
def checkcoloumn():
    global run
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"
    if col1 or col2 or col3:
        run = False
    if col1:
        if board[0]=='O':
            print("1st player won the game")
        else:
            print("2nd player won the game")
    if col2:
        if board[1]=='O':
            print("1st player won the game")
        else:
            print("2nd player won the game")
    if col3:
        if board[2]=='O':
            print("1st player won the game")
        else:
            print("2nd player won the game")        

def checktie():
    global run
    global Check_tie_list
    if len(Check_tie_list)==9:
        print("Game ended in a tie")
        run = False
board_display()
def game():
    global count
    while run:
        if count%2!=0:
            up = int(input("2nd player's turn, Select the postion you want to place your 'X'"))
            cp = up-1
            board[cp] = 'X'
        else:
            up = int(input("1st player's turn, Select the postion you want to place your 'O'"))
            if (count == 0) and (up not in Check_corner):
                print("Please select the corner position")
                continue
            cp = up - 1
            board[cp] = 'O'
        count+=1
        Check_tie_list.append(count)
        board_display()
        checkcoloumn()
        checkrow()
        checktie()
game()
    
    
    
