import pyperclip
import pyautogui

# this will show x and y coordinates of the mouse pointer, updated dynamically, 
# always printed on the same line.
# it will also copy x, y coordinates as two-integer tuple when KeyboardInterrupt happens.
def show_mouse_coord():
	while True:
		try:
			x, y = pyautogui.position()
			x_text = "X: " + str(x).rjust(4)
			y_text = " Y: " + str(y).rjust(4)
			print(x_text, end="")
			print(y_text, end="")
			print('\b' * (len(x_text) + len(y_text)), end="")
		except KeyboardInterrupt:
			pyperclip.copy("(%d, %d)" % (x, y))
			exit()

if __name__ == "__main__":
		show_mouse_coord()
