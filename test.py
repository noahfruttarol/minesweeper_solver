from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://minesweeperonline.com/')
assert 'Minesweeper Online - Play Free Online Minesweeper' in browser.title

