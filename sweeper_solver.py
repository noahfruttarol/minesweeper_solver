'''sweeper_solver.py by Noah Fruttarol'''
from minesweeper_board import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import random

DEFULT_MAX_X : int = 16 #defult board size of website
DEFULT_MAX_Y : int = 30

def get_tile_type(tile): #given a tile returns the type as an int -2 for flagged -1 for blank and n >= 0 for open
    '''get_tile_type method'''
    s : str = tile.get_attribute('class') #tile can have 3 class types "square blank", "square bombflagged", and "square open*" where 0 <= * <= 8
    num = re.findall('\d+', s) #gets the number of bombs around if open tile 
    if len(num) == 1:
        return int(num[0])
    elif s == 'square bombflagged': 
        return -2
    else:
        return -1

def is_tile_blank(tile):
    '''is_tile_blank method'''
    s : str = tile.get_attribute('class')
    if s == 'square blank': 
        return True
    else: 
        return False

def get_updates(driver): # pretty sure this is what is slowing the program down lmao
    '''get_updates method''' 
    updates : list = []
    for i in range(1,DEFULT_MAX_X+1):
        for j in range(1,DEFULT_MAX_Y+1): #goes over all the tiles to get open and flagged to give to the board class
            tile = driver.find_element(By.ID , "{}_{}".format(i,j))
            update_type = get_tile_type(tile)
            if update_type >= 0 or update_type == -2:
                update = (i,j,update_type)
                updates.append(update)
    return updates

def apply_suggestions(driver, updates : list):
    '''apply_suggestions method''' #apply suggestions form the board class
    action = ActionChains(driver)
    for x,y,change in updates:
        tile = driver.find_element(By.ID , "{}_{}".format(x,y))
        if is_tile_blank(tile):
            if change == -1:
                tile.click()#open tile
            elif change == -2:
                action.context_click(tile).perform()#flag tile
    return

def main():
    driver = webdriver.Chrome()
    driver.get('https://minesweeperonline.com/')
    assert 'Minesweeper Online - Play Free Online Minesweeper' in driver.title #opens browser and makes sure page is loaded
    gameboard = Board(DEFULT_MAX_X, DEFULT_MAX_Y) #sets up board 

    x : int = random.randrange(1,DEFULT_MAX_X+1)
    y : int = random.randrange(1,DEFULT_MAX_Y+1)
    tile = driver.find_element(By.ID , "{}_{}".format(x,y))
    tile.click() #starts by hitting a random tile
    stillUpdates : bool = True
    while(stillUpdates):
        updates : list = get_updates(driver)
        gameboard.update_board(updates)
        updates = gameboard.get_suggestions() #gives updates to board class and applys suggestions from the class
        if len(updates) > 0:
            apply_suggestions(driver, updates)
        else:
            print("Help me please!")
            print("Do I Continue(c) or Done(d)?")
            answer : str = input() #when stuck asks user for help
            if answer == 'd' or answer == 'Done':
                stillUpdates = False

if __name__ == '__main__':
    main()