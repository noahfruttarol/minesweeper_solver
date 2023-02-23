from minesweeper_board import *

gameboard = Board(4, 4)

updates = []
update = (1,1,0)
updates.append(update)
update = (2,1,0)
updates.append(update)
update = (3,1,1)
updates.append(update)
update = (1,2,0)
updates.append(update)
update = (2,2,0)
updates.append(update)
update = (3,2,1)
updates.append(update)
update = (1,3,2)
updates.append(update)
update = (2,3,2)
updates.append(update)
update = (3,3,1)
updates.append(update)
gameboard.update_board(updates)

moves = gameboard.get_suggestions()
print(moves)

updates = []
update = (1,4,-2)
updates.append(update)
update = (2,4,-2)
updates.append(update)
gameboard.update_board(updates)

moves = gameboard.get_suggestions()
print(moves)

updates = []
update = (4,2,1)
updates.append(update)
update = (4,3,0)
updates.append(update)
update = (4,4,0)
updates.append(update)
update = (3,4,1)
updates.append(update)
gameboard.update_board(updates)

moves = gameboard.get_suggestions()
print(moves)