import os

Board=[["","",""],
       ["","",""],
       ["","",""]]
player="X"
status=False
count=0


for i in range(100):
    
    print(f'{player} this is your chance:')
    row=int(input("Enter row value..0,1,2:"))
    col=int(input("Enter col value..0,1,2:"))
    os.system('cls')

# Validate input and check if the cell is empty
    if row in range(3) and col in range(3):
     if Board[row][col]=='': 
          Board[row][col]=player
          for r in Board:
           print(r)
          count+=1
         
     else:
          print('Enter valid index')
          continue
          


# Check for a win
    for i in range(3):
        # Check columns 
       if Board[0][i]==Board[1][i]==Board[2][i]==player:
          print("You are Winner")
          status=True
          break
        # Check row 
       elif Board[i][0]==Board[i][1]==Board[i][2]==player :
           print("You are Winner")
           status=True
           break
     # Check diagonals       
       elif Board[0][0]==Board[1][1]==Board[2][2]==player or Board[0][1]==Board[1][1]==Board[0][2]==player:
           print("You are Winner")
           
           status=True
           break

    # Check for a tie   
    if status:
        break
    elif count == 9:
        print("Game is Over, no one wins")
        break

 # Switch player
    if player == "X":
        player = "0"
    else:
        player = "X"
         
else:
   print("Game is Over")