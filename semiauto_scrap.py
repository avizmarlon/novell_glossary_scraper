### Novell Glosary Scraping
## by Marlon Aviz

import pyautogui
import pyperclip
from time import sleep

def pixelColor(x, y):
	x, y = pyautogui.position()
	color = pyautogui.pixel(x, y)
	return color

def altTab(arg):
	if arg == 'double':
		pyautogui.hotkey('alt', 'tab', 'tab', interval=0.20)
	elif arg == 'single':
		pyautogui.hotkey('alt', 'tab', interval=0.20)

def getText(previous_clipboard):
	print("Getting text data...")
	pyautogui.click()
	pyautogui.moveTo()
	pyautogui.moveRel(600, duration=0.05)
	sleep(0.10)
	pyautogui.click()
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')
	if pyperclip.paste() == previous_clipboard:
		print("Same text, skipping...\n")
		return "same text"
	else:
		altTab('single')
		pyautogui.hotkey('ctrl', 'end')
		pyautogui.hotkey('ctrl', 'v')
		print("Text data scraped.\n")
		altTab('single')
		return "ok"

def prepare():
	print("Starting...")
	altTab('single')
	altTab('double')
	

print("Setting global variables...")
WHITE = (255, 255, 255) # RGB value of white (constant)
coord = {
'x': 405,
'y': 581
}

prepare()

while True:
	pyautogui.moveTo(coord['x'], coord['y'], duration=0.05)
	previousClipboardText = pyperclip.paste()
	current_coord = pyautogui.position()
	coord['x'] = current_coord[0]
	coord['y'] = current_coord[1]
	if pixelColor(coord['x'], coord['y']) == WHITE:
		print("White pixel detected. Skipping...\n")
		coord['y'] += 1
		continue
	else:
		getText(previousClipboardText)
		coord['y'] += 1
