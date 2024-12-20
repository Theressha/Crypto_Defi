# Open and close Brave profiles and navigate automatically 
#To get cursor position execute in a new terminal:
# import pyautogui
# pyautogui.displayMousePosition()
# pantalla Sony Bravia
# Resolució: 1360x768
# Lletra: 100%
import pyautogui as o_bot
import time
import sys
import random
def f_open(d_pos, d_click=1):
    o_bot.moveTo(d_pos)
    o_bot.click(clicks=d_click)
left = 551, 680
right = 776, 660
try:


    time.sleep(3)
    o_bot.moveTo(right)
    time.sleep(1)
    o_bot.mouseDown(button='left')  # press the right button down
    time.sleep(3)
    o_bot.mouseUp(button='left')
    time.sleep(3)
    while True:
        o_bot.mouseDown(button='left', x=551, y=680)
        o_bot.mouseUp(button='left')
        o_bot.mouseDown(button='left', x=776, y=680)
        o_bot.mouseUp(button='left')
    
except KeyboardInterrupt:
    sys.exit()
