import pyautogui as pg
import time

time.sleep(3)

for i in range(5):
    pg.write("I Love you")
    time.sleep(0.02)
    pg.press("Enter")
