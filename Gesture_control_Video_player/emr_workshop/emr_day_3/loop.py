import time
import pyautogui

time.sleep(4)

for i in range(100):

    pyautogui.write("hello")
    key = pyautogui.press('Enter')
