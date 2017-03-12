### Novell Glosary Scraping
## by Marlon Aviz

import pyautogui
import pyperclip

def mouse_coord():
	coord = pyautogui.position()
	return coord

initial_coord = {
'x': 93,
'y': 538
}




## pseudocode
loop {
scrollDownEachNIterations (discover N)
cursorGoDown
setCurrentCoord
click
cursorGoRight
click
type(ctrl+a)
type(ctrl+c)
cursorToNotepad
click
type(ctrl+end)
type(ctrl+v)
cursor go to setCurrentCoord
}