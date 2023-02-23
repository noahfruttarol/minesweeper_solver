'''Minesweeper_board by Noah Fruttarol'''

class Tile:
    '''Tile class'''
    def __init__(self):
        self._val : int = -1 #type of tile -1 for blank, -2 for flaged, and n>=0 for number of bombs around an open tile  
        self._istDone : bool = True

    def set_tile(self, val : int):
        '''set_tile method''' #sets the value of tile to -2 for flagged or n>=0 for open
        if self._val == -1: #if blank tile can be reviled else should not be changed
            self._val = val
            return True
        else: 
            return False

    def get_value(self):
        '''get_value method'''
        return self._val

    def set_done(self):
        '''set_done method''' #sets the tile is done if there is no more changes that can be made to adjacent tiles 
        self._istDone = False

    def ist_done(self):
        '''ist_done''' #isn't done
        return self._istDone

class Board:
    '''Board class'''
    def __init__(self, sizeX : int, sizeY : int):
        self._table : list = []
        self._ym : int = sizeY
        self._xm : int = sizeX
        for i in range(self._xm):
            temp : list = []
            for j in range(self._ym):
                t = Tile()
                temp.append(t)
            self._table.append(temp)
    
    def update_board(self, updates : list):
        '''update_board method''' 
        for update in updates:
            x : int = update[0] - 1 #changes x and y as the board on the website start at 1 not 0
            y : int = update[1] - 1
            if self._valid_index(x,y):
                self._table[x][y].set_tile(update[2])
    
    def get_suggestions(self):
        '''get_suggestions method''' 
        updates : list = []
        for i in range(self._xm):
            for j in range(self._ym):
                val = self._table[i][j].get_value()
                if self._table[i][j].ist_done and val >= 0: #checks if the tile has informationa and can have adjacent tiles changed
                    adjacent : list = self._get_adjacents(i, j)
                    blanks, flags = self._count_flags(adjacent)
                    if flags == val: #checks if all bombs have been flagged
                        updates.extend(self._get_blank_updates(adjacent, -1))
                        self._table[i][j].set_done()
                    elif blanks + flags == val: #checks if all safe tiles have been opened
                        updates.extend(self._get_blank_updates(adjacent, -2))
                        self._table[i][j].set_done()
        return updates
                    

    def _get_adjacents(self, x : int, y : int):
        '''get_adjacents method''' #returns list of adjacent tiles in (x,y,val) format
        adjacent : list = []
        adjacent_index : list = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)] #list of adjacent indexs
        for x1,y1 in adjacent_index:
            if self._valid_index(x1,y1): #checks if index is valid and adds it to list
                val : int = self._table[x1][y1].get_value()
                adjacent.append((x1, y1, val))
        return adjacent

    def _valid_index(self, x,y):
        '''valid_index method'''
        return x < self._xm and x >= 0 and y < self._ym and y >= 0
    
    @staticmethod
    def _count_flags(tiles : list):
        "static count_flags method" #returns count of blank and flaged tiles from list of (x,y,val) format
        blanks : int = 0
        flags : int = 0
        for x,y,val in tiles:
            if val == -1:
                blanks += 1
            elif val == -2:
                flags += 1
        return (blanks, flags)
    
    @staticmethod
    def _get_blank_updates(tiles : list, updateType):
        '''static get_blank_updates method''' #given a list of tiles in (x,y,val) format returns a list of all blank tiles in (x,y,updateType) format updateType being -1 for open and -2 for flag 
        updates : list = []
        for x,y,val in tiles:
            if val == -1:
                temp : tuple(int, int, int) = (x+1, y+1, updateType)
                updates.append(temp)
        return updates