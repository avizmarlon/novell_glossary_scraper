import pyperclip
import pyautogui

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
