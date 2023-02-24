from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://minesweeperonline.com/')
assert 'Minesweeper Online - Play Free Online Minesweeper' in driver.title


action = ActionChains(driver)
tile = driver.find_element(By.ID , "8_15")
tile.click()#open tile 

tile = driver.find_element(By.ID , "7_17")
action.context_click(tile).perform()#flag tile

name = tile.get_attribute('class')
print(name)