import pyautogui
import time
import random
#import win32gui
#import win32con
import pygetwindow as gw # pip3 install pygetwindow

# windows = gw.getAllTitles()
# for win in windows:
#     # if str(win) != "Google Chrome": 
#     #     continue
geometry = gw.getWindowGeometry("Google Chrome")
print(f'Window title: {"Google Chrome"}')
print(f'> top-left X coordinate: {geometry[0]}')
print(f'> top-left Y coordinate: {geometry[1]}')
print(f'> width: {geometry[2]}')
print(f'> height: {geometry[3]}\n')


currentMouseX, currentMouseY = pyautogui.position()
i = 0
top_left_x = geometry[0]
width = geometry[2]
height = geometry[3]
top_left_y = geometry[1]

while i < 10:
    print(i)
    tmpX = top_left_x + random.randint(0, int(width))
    tmpY = top_left_y + random.randint(0, int(height))
    pyautogui.moveTo(tmpX, tmpY, duration=1)
    time.sleep(1)
    i += 1