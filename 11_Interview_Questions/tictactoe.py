"""
Implement tictactoe game

https://www.youtube.com/watch?v=mCnEdag893M

"""

TTT = [['_']*3, ['_']*3, ['_']*3]
choice = ""
player = 1
rounds = 0
symbol = "X"
print("Lets start game. To stop write exit")
# Start game loop
while(choice != 'exit'):
    if rounds == 9:
        print("The game is finished!!")
        break

    row = int(input("Player {} with symbol {}: Please Pick Row".format(player, symbol)))
    col = int(input("Player {} with symbol {}: Please Pick Column".format(player, symbol)))

    if row == '-1' or col == '-1':
        break


    if (TTT[row][col] == '_'):
        TTT[row][col] = symbol
        rounds += 1

        if player == 1:
            player = 2
            symbol = "O"
        else:
            player = 1
            symbol = "X"
    else:
        print("Oops you picked a wrong place. Exiting")
        break
    for i in TTT:
        print(i)



