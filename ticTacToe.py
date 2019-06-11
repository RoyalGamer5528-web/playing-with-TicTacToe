board = [" 1 " , " 2 " , " 3 ", " 4 " , " 5 " , " 6 ",   " 7 " , " 8 " , " 9 "]



def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    
    
def game_still_going():
    no=0
    checker=False
    while checker!=True and no<=8:
        print("\n.          enter position.....      \n")
        pos=int(input())
        print("\n")
        #gets the character to be printed at pos
        #calls is_pos_empty() , gets true if empty , else false , if true , continue
        bol=is_pos_empty(pos-1)
        if bol==False:
            print("position is already taken")
            continue            
        symbol=player_flip(no)
        no=no+1
        board[pos-1]=symbol
        checker=is_game_over()
        display_board()
    #calls game_over() , which declare the winner
    game_over()


def is_pos_empty(temp):
    if board[temp]==" X " or " O " :
        ret=True
    else:
        ret=False
    return ret
    

#players turn..
def player_flip(no):
    if(no%2==0):
        ret=" x "
    else:
        ret=" o "
    return ret  
    
    
def comparer(one,two,three):
    temp=False
    if((one==two) and (two==three)):
        temp=True
        print("the winner is "+ one)
    return temp  
    
     
    
def game_row():
    ret=False
    for i in range(0,7):
        if comparer(board[i],board[i+1],board[i+2]):
            ret=True
            break
        else:
            i=i+3
    return ret
    
            
            
def game_column():
    ret=False
    for i in range(0,3):
        if comparer(board[i],board[i+3],board[i+6]):
            ret=True
            break
        else:
            i=i+1
    return ret
            
       
def game_left_diagonal():
    ret=False
    i=0
    if comparer(board[0],board[4],board[8]):
        ret=True
    return ret
        
        
def game_right_diagonal():
    ret=False
    i=2
    if comparer(board[2],board[4],board[6]):
        ret=True
    return ret


    
def game_over():
    if game_row():
        print("row")
    elif game_column():
        print("column")
    elif game_left_diagonal():
        print("left diaginal")
    elif game_right_diagonal():
        print("right diagonal")
    else:
        print("ohh , such a tough competition , game tied..")
        
        
def is_game_over():
    ret=False
    if game_row()==True or game_column()==True or game_left_diagonal()==True or game_right_diagonal()==True:
        ret=True
    return ret   
        
        


    
    
    
display_board()
game_still_going()